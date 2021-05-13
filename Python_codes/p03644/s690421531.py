N=int(input())
a=[]
for b in range(1,N+1,1):
  count=0
  while b%2 == 0:
    count+=1
    b/=2
  a.append(count)

print(a.index(max(a))+1)