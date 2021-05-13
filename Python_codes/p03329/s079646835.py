n = int(input())
ans = n

for i in range(n + 1):
    j = n - i
    cnt = 0
    while i:
        cnt += i%6
        i = i//6
    while j:
        cnt += j%9
        j = j//9
    ans = min(ans, cnt)

print(ans)