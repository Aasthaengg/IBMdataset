M = 10**9 + 7
s = int(input()) - 1
a = [0, 0] + [1] * (s - 1)
for i in range(s - 2):
  a[i + 3] = (a[i + 3] + a[i]) % M
  a[i + 1] = (a[i + 1] + a[i]) % M
print(a[s])
