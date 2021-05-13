N=int(input())
A=[int(input()) for i in range(N)]
for i in range(N):
  if A[i]%2==1:
    print('first')
    exit()
print('second')