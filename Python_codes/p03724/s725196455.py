n, m = map(int, input().split())
c = [0] * (n + 1) 
for i in range(m):
    a, b = map(int, input().split())
    c[a] += 1
    c[b] += 1

flag = True
for i in range(n + 1):
    if c[i] % 2 == 1:
        flag = False
        break

if flag:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
