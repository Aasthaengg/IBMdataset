from collections import defaultdict

s = int(input())
D = defaultdict(int)
D[s] += 1
ans = 1

def f(a):
  if a%2 == 0:
    return a//2
  else:
    return 3*a + 1

while True:
  s = f(s)
  ans += 1
  if D[s] == 1:
    print(ans)
    break
  D[s] += 1