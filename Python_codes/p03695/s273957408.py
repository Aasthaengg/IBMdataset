N = int(input())
A = list(map(int, input().split()))
X = [0 for i in range(8)]
cnt = 0
for a in A:
  if a >= 3200:
    cnt += 1
  else:
    X[a // 400] = 1
s = sum(X)
if s == 0:
  print(str(1) + " " + str(cnt))
else:
  print(str(s) + " " + str(s + cnt))