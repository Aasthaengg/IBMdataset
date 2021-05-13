n, k, c = map(int, input().split())
s = input()
L = [-1]*k
R = [-1]*k
now = 0
cnt = 0
while now < n and cnt < k:
  if s[now] == "o":
    L[cnt] = now
    cnt += 1
    now += c+1
  else:
    now += 1
now = n-1
cnt = k-1
while now >= 0 and cnt >= 0:
  if s[now] == "o":
    R[cnt] = now
    cnt -= 1
    now -= c+1
  else:
    now -= 1
A = []
for i in range(k):
  if L[i] == R[i]:
    A.append(L[i]+1)
print(*A, sep="\n")