n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
MIN = []
MAX = []
MIN.append(t[0])
MAX.append(t[0])

for i in range(1,n):
  if t[i] == t[i-1]:
    MIN.append(1)
    MAX.append(t[i])
  else:
    MIN.append(t[i])
    MAX.append(t[i])
MIN[-1] = max(MIN[-1],a[-1])
MAX[-1] = min(MAX[-1],a[-1])
for i in range(n-1,0,-1):
  if a[i-1] == a[i]:
    MAX[i-1] = min(MAX[i-1],a[i-1])
  else:
    MIN[i-1] = max(MIN[i-1],a[i-1])
    MAX[i-1] = min(MAX[i-1],a[i-1])
ans = 1
for i,j in zip(MIN,MAX):
  diff = j-i+1
  if diff <= 0:
    print(0)
    exit()
  ans *= diff
  ans %= mod
print(ans)