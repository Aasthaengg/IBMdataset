MAX = pow(10,18)
def main():
    N = int(input())
    A = list(map(int,input().split()))

    if 0 in A:
        print(0)
        return

    ans = 1
    for a in A:
        ans *= a
        if ans > MAX:
            print(-1)
            return

    print(ans)

main()
