N = int(input())
A = list(map(int,input().split()))
pA = [(-1)**(0)*A[0]]
mA = [(-1)**(0+1)*A[0]]
for i in range(1,N):
  pA.append((-1)**(i)*A[i] + pA[i-1])
  mA.append((-1)**(i+1)*A[i] + mA[i-1])

ansl = []
for s in range(N):
  if s == 0:
    ansl.append(pA[N-1])
  else:
    if s%2 == 0:
      ansl.append( pA[N-1]-pA[s-1] + mA[s-1] )
    elif s%2 == 1:
      ansl.append( mA[N-1]-mA[s-1] + pA[s-1] )
print(*ansl)    