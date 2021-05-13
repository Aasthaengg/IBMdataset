N, K = map(int, input().split())
Ans = [0] * (N+1)
for _ in range(K):
    _ = input()
    A = list(map(int, input().split()))
    for a in A:
        Ans[a] = 1
print(Ans.count(0)-1)
