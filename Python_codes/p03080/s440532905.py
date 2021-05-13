N = int(input())
S = input()

cnt = 0
for s in S:
  if "R" == s:
    cnt += 1

if cnt > N - cnt:
  print("Yes")
else:
  print("No")