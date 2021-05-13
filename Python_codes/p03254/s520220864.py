n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

s = 0
cnt = 0
for i in a:
    s += i
    if s > x:
        break
    cnt += 1

if s < x:
    cnt -= 1    
print(cnt)
