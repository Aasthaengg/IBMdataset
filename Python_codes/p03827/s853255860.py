N = int(input())
S = str(input())
cnt = 0

ans = []
for i in range(0,N):
  if S[i] == "I":
    cnt = cnt+1
  elif S[i] == "D":
    cnt = cnt-1
  ans.append(cnt)

if max(ans) <= 0:
  print("0")
else:
  print(max(ans))