N,K = map(int,input().split())
S = list(str(input()))
arr = [0,0]
D = [0,0]
cnt = 0
d = 0

for i in range(len(S)):
  a = int( S[i] )
  if a == 1:
    cnt += 1 + d
    if d > 0:
      D.append(d)
    d = 0
  elif a == 0 and d == 0:
    arr.append(cnt)
    d += 1
  else:
    d += 1
if a == 1:
  arr.append(cnt)
if a == 0:
  arr.append(cnt+d)
arr.sort()

ans = 0
for i in range(len(arr)-K-1):
  a = arr[i+K+1] - arr[i]
  b = D[i]
  ans = max(a-b,ans)
if len(arr) <= K:
  ans =  N
print(ans)