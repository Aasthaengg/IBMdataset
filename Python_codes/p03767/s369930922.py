N = int(input())
A = list(map(int, input().split()))
A_tmp = sorted(A)
Cnt = 0
for i in range(1,N+1):
  Cnt +=A_tmp[3*N-2*i]
print(Cnt)