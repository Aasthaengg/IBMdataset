N,K,C= map(int, input().split())
S=input()
A=[]
for i in range(N):
  if S[i]=='o':
    A.append(i)
M=[]
d=0
cnt=0
for i in A:
  if d<=i:
    M.append(i)
    d=i+C+1
    cnt+=1
  if cnt==K+1:
    print()
    exit()
    
U=[]
d=N-1
cnt=0
for i in A[::-1]:
  if i<=d:
    U.append(i)
    d=i-C-1
    cnt+=1
  if cnt==K+1:
    print()
    exit()
D=set(M)&set(U)
D=sorted(D)
for i in D:
  print(i+1)