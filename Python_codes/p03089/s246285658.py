n=input()
b=list(map(int,input().split()))
a=[]
while b:
  c=0
  for i,j in enumerate(b,1):
    if i==j:c=i
  if c==0:
    print(-1)
    exit()
  a+=[b.pop(c-1)]
print(*a[::-1],sep='\n')