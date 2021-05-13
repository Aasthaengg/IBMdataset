n,k = map(int, input().split())
ans = 0
num = [i for i in range(1, k+1)]
while num[-1] <= n:

    num = [i+1 for i in num]
    ans += 1
print(ans)