n=int(input());a=list(map(int,input().split()))
count=0
result=0
for i in range(1, n):
  if a[i-1]>=a[i]:
    count+=1
  else:
    result=max(result,count)
    count=0
print(max(result,count))