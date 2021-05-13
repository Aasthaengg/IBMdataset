N, A, B = map(int, input().split())
ans = 0
for i in range(1,N+1):
    a = i
    tot = 0
    while a > 0:
        tot += a%10
        a //= 10
    if A <= tot <= B:
        ans += i
print(ans)