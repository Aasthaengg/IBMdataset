n = int(input())
s = []
for i in range(n):
  s.append(input())
  
m = int(input())
t = []
for i in range(m):
  t.append(input())

count = 0
for i in range(n):
  count = s.count(s[i]) - t.count(s[i]) if count < s.count(s[i]) - t.count(s[i]) else count
print(count)