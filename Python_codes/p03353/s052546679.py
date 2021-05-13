s = input()
k = int(input())
t = []
n = len(s)
for i in range(n):
  for j in range(1, k + 1):
    if i + j > n:
      continue
    t.append(s[i:i+j])
t = sorted(list(set(t)))
print(t[k - 1])
