N=int(input())
ct=0
for i in range(1,N+1):
  l=len(str(i))
  if l%2==1:
    ct+=1
print(ct)