N=int(input())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
A,B=[],[]
for i in range(N):
  if i % 2 == 0:
    A.append(a[i])
  else:
    B.append(a[i])
print(sum(A)-sum(B))