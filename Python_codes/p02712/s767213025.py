n = int(input())
ans = 0

for i in range(n+1):
    if i%15 == 0:continue
    elif i%3 == 0:continue
    elif i%5 == 0:continue
    else:ans += i

print(ans)