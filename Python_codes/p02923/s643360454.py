n = int(input())
h= list(map(int, input().split()))
ans=0
count=0
for i in range(1,n):
  if h[i]<=h[i-1]:
    count+= 1
  else:
    count=0
  if ans<count:
    ans=count
print(ans)