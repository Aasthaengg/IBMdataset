N=int(input())
b=list(map(int,input().split()))
c=len(b)
d=[]

for i in range(N):
  c = len(b)
  for j in range(c):
    if b[c-j-1]==c-j:
      d.append(b.pop(c-j-1))
      break
      
if b==[]:
  for num in d[::-1]:
    print(num)
else:
  print(-1)