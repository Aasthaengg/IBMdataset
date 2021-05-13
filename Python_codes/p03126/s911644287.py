n, m = map(int, input().split())

l = [0] * (m+1)
for i in range(n):
  inp = list(map(int, input().split()))
  for j in range(1, inp[0]+1):
    l[inp[j]] += 1
ans = 0
#print(l, n)
for i in range(1, m+1):
  if l[i] == n:
    ans += 1
print(ans)