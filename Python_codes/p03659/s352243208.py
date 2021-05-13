N = int(input())
A = list(map(int,input().split()))
S = [0]
for i in range(N):
  temp = S[-1]+A[i]
  S.append(temp)
total = sum(A)
target = total//2
INF = float("inf")
ans = INF

for i in range(N-1): #0からN-1
  temp = abs(total-2*S[i+1])
  ans = min(ans,temp)
print(ans)