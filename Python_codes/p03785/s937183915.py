N,C,K = map(int,input().split())
A = []
for i in range(N):
  temp = int(input())
  A.append(temp)
A.sort()
ans = 1
nxt = A[0]+K
cus = 0
for i in range(N):
  if A[i] <= nxt and cus < C:
    cus +=1
    continue
  else:
    nxt = A[i]+K
    cus = 1
    ans += 1
print(ans)