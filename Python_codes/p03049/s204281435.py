n = int(input())
a = b = ab = ans = 0
for _ in range(n):
  t = input()
  ans += t.count("AB")
  if t[0] == "B":
    if t[-1] == "A":
      ab +=1
    else:
      b += 1
  elif t[-1] =="A":
    a += 1
if ab > 0:
  ans += ab-1
  if a > 0:
    ans += 1
    a -= 1
  if b > 0:
    ans += 1
    b -= 1
print(ans + min(a,b))