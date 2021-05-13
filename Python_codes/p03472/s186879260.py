N,H=map(int,input().split())
A=[]
B=[]
for _ in range(N):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)

B.sort(reverse=True)
A.sort(reverse=True)
B=[x for x in B if x>A[0]]
cnt=0
for i in range(len(B)):
  H-=B[i]
  cnt+=1
  if H<=0:
    print(cnt)
    exit()

A.sort(reverse=True)
print(cnt-(-H//A[0]))