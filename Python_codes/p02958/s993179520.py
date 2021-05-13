n = input()
p = list(map(int,input().split()))

ps = sorted(p)

count = 0
for q, qs in zip(p, ps):
  if q != qs:
    count += 1
    
print('YES' if count <= 2 else 'NO')