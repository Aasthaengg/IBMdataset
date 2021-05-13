def resolve():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    sub = []
    ans = []
    for i in range(N):
        sub.append(T-H[i]*0.006)
    for j in range(N):
        ans.append(abs(A-sub[j]))
    print(ans.index(min(ans))+1)
resolve()