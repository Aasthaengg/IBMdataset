k, t = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
mx = a[0]
sa = sum(a[1:])
print(max(mx-sa-1, 0))