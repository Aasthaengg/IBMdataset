a, b, k=map(int, input().split())
cnt=0
x=max(a,b)
y=min(a,b)

for i in range(y, 0, -1):
  if x%i==0 and y%i==0:
    cnt+=1
  if cnt==k:
    print(i)
    exit()