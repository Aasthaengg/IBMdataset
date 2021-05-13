N = int(input())
a = list(map(int, input().split()))
a = sorted(a)
l = len(a)
d = a[l-1]-a[0]
print(d)