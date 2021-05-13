n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
pt=0
for i in a[::2]:
  pt+=i
for i in a[1::2]:
  pt-=i
print(pt)