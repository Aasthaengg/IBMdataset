N,A,B = map(int, input().split())
H = [int(input()) for i in range(N)]

def check(X):
    """ X回以下の爆発で全滅するか """
    ans = 0
    for h in H:
        cnt = ((h - B * X) + (A - B) - 1) // (A - B)
        ans += max(0, cnt)
    return ans <= X

def main():
    ng = 0
    ok = 10 ** 10
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == "__main__":
    main()