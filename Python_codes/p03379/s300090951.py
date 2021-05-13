N=int(input())
A=list(map(int, input().split()))
B=sorted(A)
l=B[N//2-1]
r=B[N//2]
for i in range(N):
  a=A[i]
  if a<=l:
    print(r)
  else:
    print(l)