n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in range(n-2):
  for j in range(i+1,n-1):
    u=l[i]-l[j]
    if l[j+1]<=u:
      break
    ok=j+1
    ng=n
    while ng-ok>1:
      center=(ok+ng)//2
      if l[center]>u:
        ok=center
      else:
        ng=center
    c+=ng-j-1
print(c)    