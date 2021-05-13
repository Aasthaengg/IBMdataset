N=int(input())
*A,=map(int,input().split())

sumA = sum(A)

cum=[0]
for i in range(N):
  cum.append(cum[-1]+A[i])

print(min([abs(cum[i]-(sumA-cum[i])) for i in range(1,N+1)]))