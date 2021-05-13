N=int(input())
A=list(int(x) for x in input().split())
A.sort()
sum = 0
for i in range(N-1):
  k=i+1
  sum+=A[N-int(k/2)-1]
print(sum)