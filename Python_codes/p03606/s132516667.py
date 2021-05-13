n = int(input())

# はこ
l = []
s = 0

for i in range(n):
  l.append(input().split())
  
for i in range(n):
  s += int(l[i][1]) - int(l[i][0]) + 1
  
print(s)