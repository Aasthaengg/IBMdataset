n = int(input())
A = list(map(int,input().split()))
A.append(0)
T = []

ans = 0
for i in range(n+1):
  if A[i]==(i+1):
    T.append(1)
  else:
    T.append(0)    
for i in range(n+1):
  if T[i]:
    ans+=1
    T[i+1]=0

print(ans)