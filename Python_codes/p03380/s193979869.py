n = int(input())
a = list(map(int,input().split()))
a.sort()
ma = a[-1]
mn = float("inf")
mni = -1
for i in range(n-1):
  if abs(2*a[i]-ma) < mn:
    mn = abs(2*a[i]-ma)
    mni = i
print(ma,a[mni])