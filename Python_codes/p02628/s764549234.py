N, K=list(map(int, input().split(" ")))

P=list(map(int, input().split(" ")))

sum=0
for i in range(K):
  sum=sum+sorted(P)[i]

print(sum)