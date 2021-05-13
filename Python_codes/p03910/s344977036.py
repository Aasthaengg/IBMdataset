N=int(input())

sum=0
a=[]
i=1
while sum<=N:
  sum+=i
  a.append(i)
  i=i+1
if sum>N:
  a.remove(sum-N)
#print(sum)
print(*a)