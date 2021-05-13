N = int(input())
li = list(map(int, input().split()))
count = 0
flag = False

while True:
  for i in range(N):
    if(li[i]%2!=0):
      flag = True
    li[i] /= 2
  
  if(flag):
    break
    
  count+=1

print(count)