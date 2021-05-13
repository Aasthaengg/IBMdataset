N = int(input())
A = [0, 0, 0, 0, 0]
for i in range(N):
  s = input()
  if s[0] == "M":
    A[0] += 1
  elif s[0] == "A":
    A[1] += 1
  elif s[0] == "R":
    A[2] += 1
  elif s[0] == "C":
    A[3] += 1
  elif s[0] == "H":
    A[4] += 1
ans = 0
for i in range(3):
  for j in range(i+1, 4):
    for k in range(j+1, 5):
      ans += A[i] * A[j] * A[k]
print(ans)