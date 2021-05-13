import sys
N=int(input())
A=input()
B=input()
for i in range(N+1):
  if A[i:N]==B[0:N-i]:
    print(N+i)
    sys.exit()