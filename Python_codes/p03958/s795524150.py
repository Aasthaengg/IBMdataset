k, t = map(int, input().split())
a = list(map(int, input().split()))
aa = max(a)
print(max(2*aa-k-1, 0))
