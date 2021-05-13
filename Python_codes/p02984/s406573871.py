N=int(input())
A=list(map(int, input().split()))
M=[0]*N
maxi=sum(A)

M[0]=maxi//4
tmp=10**9

while M[0]/2 != tmp:
  for i in range(1,N):
    M[i]= 2*(A[i-1]-M[i-1]//2)
  tmp = A[-1] - M[N-1]//2
  #print(M,tmp)
  if M[0] != tmp*2:
    M[0] = (M[0]+tmp*2)//2
    if M[0]%2!=0:
      M[0] +=1
else:
  print(*M)