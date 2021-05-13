N = int(input())
S = [input() for _ in range(N)]
count = 0
l = []
A,B,BA = 0,0,0
for s in S:
  c = s.count("AB")
  count += c
  if s[-1] == "A" or s[0] == "B":
    l.append(s[0] + s[-1])
    if s[-1] == "A" and s[0] == "B":
      BA += 1
    elif s[-1] == "A":
      A += 1
    elif s[0] == "B":
      B += 1
ans = 0
if BA == 0:
  ans = min(A,B)
elif A+B > 0:
  ans = BA + min(A,B)
elif  A+B == 0:
  ans = BA -1 + min(A,B)
print(count + ans)