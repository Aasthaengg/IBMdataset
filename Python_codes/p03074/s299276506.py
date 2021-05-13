n, k = map(int, input().split())
s = input()

key = [0]
for i in range(1, n):
  if s[i] != s[i-1]:
    key.append(i)
key.append(n)

m, r = 0, len(key)-1
ans = 0
while True:
  if m == 0 and s[0] == "0":
    p = m+2*k
    if ans < key[min([p, r])] - key[m]:
      ans = key[min([p, r])] - key[m]
    m += 1
  else:
    p = m+2*k+1
    if ans < key[min([p, r])] - key[m]:
      ans = key[min([p, r])] - key[m]
    m += 2
  if p >= r:
    break

print(ans)