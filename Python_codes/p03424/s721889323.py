N = int(input())
S = list(input().split())
flag = 0
for i in range(N):
  if S[i] == "Y":
    flag += 1
if flag > 0:
  print("Four")
else:
  print("Three")