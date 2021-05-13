ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
s = [_ for _ in input()]

e = [0]
w = [0]

for si in s:
  if si == 'E':
    e.append(e[-1]+1)
    w.append(w[-1])
  if si == 'W':
    w.append(w[-1]+1)
    e.append(e[-1])

# print(e)
# print(w)

mn = 10**7

for i in range(n):
  cost = w[i] + e[n]-e[i+1]
  mn = min(cost,mn)

print(mn)