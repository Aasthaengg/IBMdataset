K, T = map(int,input().split())
A = list(map(int,input().split()))
ans = max(0, 2 * max(A) - sum(A) - 1)
print(ans)