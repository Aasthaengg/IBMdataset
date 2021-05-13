def agc024_b():
    n = int(input())
    P = [int(input())-1 for _ in range(n)]  # 0 .. n-1 にしておく
    if n == 1: return print(0)

    A = [0]*n  # 登場するindex
    for i, p in enumerate(P):
        A[p] = i

    cnt = 0  # iの登場順がi-1より後ろが連続する回数
    cmax = 0
    for i in range(1, n):
        if A[i-1] < A[i]:
            cnt += 1
        else:
            cmax = max(cmax, cnt)
            cnt = 0
    else:
        cmax = max(cmax, cnt)

    ans = n - (cmax + 1)
    print(ans)

if __name__ == '__main__':
    agc024_b()