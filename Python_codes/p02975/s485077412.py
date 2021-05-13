N=int(input())
A=list(map(int, input().split()))

a=A[0]
for i in range(N-1):
  a=a^A[i+1]
if a==0:
  print("Yes")
else:
  print("No")
