N = int(input())
S = input()
lb = 0
rw = sum([s == "." for s in S])
ans = rw

for s in S:
  if s == ".":
    rw -= 1
  else:
    lb += 1
  ans = min(ans, rw+lb)
print(ans)