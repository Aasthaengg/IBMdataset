n = int(input())
march = {}
for s in "MARCH":
  march[s] = 0
for _ in range(n):
  s = input()[0]
  if s in "MARCH":
    march[s] += 1
ans = 0
for i in range(5):
  s1 = "MARCH"[i]
  n1 = march[s1]
  for j in range(i + 1, 5):
    s2 = "MARCH"[j]
    n2 = march[s2]
    for k in range(j + 1, 5):
      s3 = "MARCH"[k]
      n3 = march[s3]
      ans += n1 * n2 * n3
print(ans)