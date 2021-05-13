n = int(input())
s = input()
cnt = s.count('R') * s.count('G') * s.count('B')
for i in range(n - 1):
  for j in range(i + 1, n):
    if 2 * j - i <= n - 1 and len(set([s[i], s[j], s[2 * j - i]])) == 3:
      cnt -= 1
print(cnt)