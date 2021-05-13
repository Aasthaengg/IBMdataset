d = int(input())

ans = 'Christmas'
eve = 25 - d

for i in range(eve):
  ans += ' Eve'

print(ans)