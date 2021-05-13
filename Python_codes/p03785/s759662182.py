N,C,K = map(int,input().split())

T = sorted([int(input()) for _ in range(N)])
ans = 1
count = 0
time = 0
start = -1
for i in range(N):
  if start == -1:
    start = i
  if i != N-1:
    if T[i+1] > T[start] + K or i+1 -start == C:
      ans += 1
      start = -1
  
print(ans)