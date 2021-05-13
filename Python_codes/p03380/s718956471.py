n = int(input())
a = list(map(int, input().split()))
ma = max(a)
a.sort(key=lambda x:abs(x-ma/2))
r = a[0] if a[0]!=ma else a[1]
print(ma, r)