N = int(input())
li = list(map(int,input().split()))

count = 0
flag = False

while flag==False:
  for i in range(N):
    if li[i]%2==0:
      li[i]=li[i]/2
    else:
      flag=True
        
  if flag==False:
    count+=1

print(count)