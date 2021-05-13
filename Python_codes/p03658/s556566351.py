N,K = map(int,input().split())

l=list(map(int, input().split()))
l=sorted(l)[::-1]

sum=0
for i in range(K):
  sum=sum+l[i]
  
print(sum)
