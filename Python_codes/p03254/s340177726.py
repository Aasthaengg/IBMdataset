n, x = map(int, input().split())
s = list(map(int, input().split()))

s.sort()
cnt = 0

for i in range(n):
    if x >= s[i]: 
        x -= s[i]
        cnt += 1
    else:
        x = 0
        break

if x > 0:
    cnt -= 1

print(cnt)
