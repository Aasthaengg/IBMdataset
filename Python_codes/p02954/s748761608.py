s = input()
n = len(s)
rl = []
ll = []
c = 0
b = "R"
for i in range(n):
  if s[i] == b:
    c += 1
  else:
    if b == "R":
      rl.append(c)
      b = "L"
    else:
      ll.append(c)
      b = "R"
    c = 1
ll.append(c)
ans = []
for i,j in zip(rl,ll):
  ans += [0]*(i-1) + [i-i//2+j//2] + [i//2+j-j//2] + [0] *(j-1)
print(*ans)