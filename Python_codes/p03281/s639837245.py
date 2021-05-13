n = int(input())

p = [2*i+1 for i in range((n+1)//2)]
ans = 0
for i in p:
    j = 1
    cnt = 0
    while j <= i:
        if i%j == 0:
            cnt += 1
        j += 2
    if cnt == 8:
        ans += 1

print(ans)