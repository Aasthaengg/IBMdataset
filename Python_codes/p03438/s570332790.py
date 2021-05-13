n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = sum(b)-sum(a)
c,d = 0,0
for i in range(n):
  e = b[i]-a[i]
  if e<=0:
    d -= e
  else:
    c+= (e+1)//2
    d+= e%2 
print("Yes" if k>=c and k>=d else "No")