n = int(input())
a = list(map(int, input().split()))
lis = [0]*(n+1)
lis[0] = 3
ans = 1
mod = 10**9 + 7
for i in range(n):
    x = lis[a[i]]
    if x == 0:
        print(0)
        exit()
    else:
        ans *= x
        ans %= mod
        lis[a[i]] -= 1
        lis[a[i] + 1] += 1
print(ans)
