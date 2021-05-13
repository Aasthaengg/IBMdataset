N,K=map(int, input().split())
x = list(map(int, input().split()))
sum=0
x=sorted(x)
for i in range(K):
  sum+=x[i]
print(sum)