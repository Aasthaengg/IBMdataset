n = int(input())
c = input()
r_count = c.count('R')
ans = 0

if r_count == 0:
    print(0)
    exit()

for ci in c:
    if ci == 'W':
        ans += 1
    r_count -= 1
    if r_count == 0:
        print(ans)
        exit()
print(ans)        