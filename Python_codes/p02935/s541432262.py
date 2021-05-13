N = int(input())
A = list(map(int,input().split()))
A.sort()
tmp = A[0]
for i in range(1,N):
  tmp = (tmp+A[i])/2
print(tmp)