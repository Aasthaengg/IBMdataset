n=int(input())
a=[1]
while sum(a) < n:
  a.append(a[-1]+1)
if sum(a) != n:
  b=sum(a)-n
  a[b-1:b]=[]
print(*a,sep="\n")