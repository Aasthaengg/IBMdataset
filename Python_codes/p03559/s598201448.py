import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()

BC = {}
for i in range(N):
  rank = N - bisect.bisect_right(C, B[i])
  BC[B[i]] = rank
#print(BC)
BCS = [0 for _ in range(N)]
BCS[N-1] = BC[B[N-1]]
for i in range(N-2,-1,-1):
  BCS[i] =  BCS[i+1] + BC[B[i]]
#print(BCS)

ans = 0
for i in range(N):
  rank = bisect.bisect_right(B, A[i])
  if rank < N:
    ans += BCS[rank]
print(ans)