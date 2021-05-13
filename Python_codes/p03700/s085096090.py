def bisect(f, ok, err):
    while abs(ok - err) > 1:
        m = (ok + err) // 2
        if f(m):
            ok = m
        else:
            err = m
    return ok

def main():
    N, A, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    A -= B
    def f(n):
        return sum((max(0,h-B*n)+A-1)//A for h in H) <= n
    print(bisect(f, 10**9+1, 0))

if __name__ == "__main__":
    main()