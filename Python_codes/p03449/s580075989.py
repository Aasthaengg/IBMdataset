def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(sum(A[:i+1])+sum(a[i:]))
    print(max(ans))
resolve()