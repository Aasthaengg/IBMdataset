#n = (m*k+1)*k**t
def divisors(n):
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n//i)
    return ans
n = int(input())
ans = 0

#t = 0
ans += len(divisors(n-1)) - 1

#t > 0
for k in divisors(n):
    if k == 1:
        continue
    temp_n = n
    while temp_n % k == 0:
        temp_n /= k
    if temp_n % k == 1:
        ans += 1
print(ans)