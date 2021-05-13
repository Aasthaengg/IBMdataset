def main():
    N, M, X = map(int, input().split())
    a = list(map(int, input().split()))
    if X < a[0] or a[M-1] < X:
        print(0)
        return
    else:
        for i in range(M):
            if X < a[i]:
                t = i
                break
        b = M - t
        f = t
        print(min(f, b))
main()