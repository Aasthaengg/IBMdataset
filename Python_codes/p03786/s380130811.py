import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
a.sort()
cs = [0] * (N + 1)
for i in range(N): cs[i + 1] = cs[i] + a[i]
#print(cs, a)
res = 0
for i in range(1, N):
  if cs[i] * 2 >= a[i]: res += 1
  else: res = 0
print(res + 1)