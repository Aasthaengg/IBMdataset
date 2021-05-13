digit = int(input())
li = list(input().split(" "))
li = [int(i) for i in li]

count = 0
flag = False

while flag==False:
  for i in range(digit):
    if li[i]%2==0:
      li[i]=li[i]/2
    else:
      flag=True
        
  if flag==False:
    count+=1

print(count)