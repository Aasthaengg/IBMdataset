N, K = map(int, input().split())

S = input()

cnt = 0
b = S[0]

for i in range(1,N):
  if b != S[i]:
    cnt += 1
  b = S[i]
  
if cnt % 2 == 1:
  if K > cnt//2:
    print(N-1)
  else:
    print(N-2*(cnt//2+1)+2*K)
else:
  if K >= cnt//2:
    print(N-1)
  else:
    print(N-cnt+2*K-1)
