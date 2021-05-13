def pr(x):
    cnt = 0
    for i in range(1, int(x**0.5)+1):
        if i**2 == x:
            cnt += 1
        elif x % i == 0:
            cnt += 2
    return cnt

n = int(input())
ans = 0
for i in range(1, n+1, 2):
    if pr(i) == 8:
        ans += 1
print(ans)