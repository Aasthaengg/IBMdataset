h=int(input())
cnt=0
while h:
  h//=2
  cnt+=1
print(2**cnt-1)