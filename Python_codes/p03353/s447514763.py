s = input()
n = int(input())

t = set()
for i in range(len(s)):
  for j in range(i + 1, i + n + 1):
    t.add(s[i:j])

l = list(t)
l.sort()
print(l[n - 1])

