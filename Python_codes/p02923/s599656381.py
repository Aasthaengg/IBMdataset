n=int(input())
h=list(map(int,input().split()))

step=[]

for i in range(n-1):
  if h[i]<h[i+1]:
    step.append(0)
  else:
    step.append(1)

a=[i for i, x in enumerate(step) if x==0]

ans=[]

for i in range(len(a)):
  if i==0:
    d=a[0]
    ans.append(d)
  else:
    b=a[i]-a[i-1]
    ans.append(b)
    

if not a:
  print(n-1)
else:
  ans.append((n-1)-a[-1])
  print(max(ans)-1)