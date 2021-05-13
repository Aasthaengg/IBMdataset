N, K = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
ans = sum(lst[:K])
print(ans)