n = int(input())
s = input()
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
for t in s:
  ans += l[l.index(t)+n]
print(ans)