n=int(input())
kot="Yes"
at,a1,a2=0,0,0
for i in range(n):
  a=list(map(int,input().split()))
  a[0]=a[0]-at
  a[1]=a[1]-a1
  a[2]=a[2]-a2
  gou=max(a[1]+a[2],(-1*a[1])+a[2],a[1]+(-1*a[2]),(-1*a[1])+(-1*a[2]))
  if a[0]%2!=(gou)%2:
    kot="No"
    break
  if a[0] < gou:
    kot="No"
    break
  at,a1,a2=a
print(kot)