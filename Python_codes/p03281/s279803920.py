def yakusuu(n):
    cnt = 0
    for i in range(1,n+1):
        if n % i == 0:
            cnt += 1
    return cnt
        

N = int(input())
ans = 0
for i in range(1,N+1):
    if i % 2 != 0:
        if yakusuu(i) == 8:
            ans += 1
print(ans)
