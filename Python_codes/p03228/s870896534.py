a,b,k = map(int, input().split())
cnt=0
while True:
  if a%2==1:
    a-=1
  half=a//2
  a-=half
  b+=half
  cnt+=1
  if cnt==k:
    break
  if b%2==1:
    b-=1
  half=b//2
  b-=half
  a+=half
  cnt+=1
  if cnt==k:
    break  
print(a,b)
