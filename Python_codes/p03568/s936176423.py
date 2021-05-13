n=int(input())
li=list(map(int,input().split()))
ev=0
for i in li:
  if i%2==0:
    ev+=1
print(3**n-2**ev)