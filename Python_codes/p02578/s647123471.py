n=int(input())
a = list(map(int,input().split()))
step=[0]*n
for i in range(n-1):
  step[i+1]+=a[i]+step[i]-a[i+1]
  if step[i+1]<0:
    step[i+1]=0
    
total=sum(step)
print(total)