n = int(input())
cnt = 0
p = [int(x) for x in input().split()]
for i in range(n-2):
  s = p[i:i+3]
  if (s[0] < s[1] and s[1] < s[2]) or (s[0] > s[1] and s[1] > s[2]):
    cnt += 1
print(cnt)