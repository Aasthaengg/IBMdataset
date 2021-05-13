def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

n = int(input())
if n == 1:
    print(1)
    exit()
cnt = [0] * (n+1)
for i in range(1, n+1):
    val = 1
    arr = factorization(i)
    for j in arr:
        cnt[j[0]] += j[1]
ans = 1
for i in range(2, n+1):
    ans *= cnt[i] + 1
    if ans >= 10**9+7:
        ans %= 10**9+7
print(ans)
