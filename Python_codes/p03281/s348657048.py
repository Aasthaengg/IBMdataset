N = int(input())

def make_divisors(n):
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans += 1
            if i != n // i:
                ans += 1
    return ans

ans = 0
for i in range(1,N+1):
    if (i %2 ==1) and (make_divisors(i) ==8):
        ans += 1

print(ans)