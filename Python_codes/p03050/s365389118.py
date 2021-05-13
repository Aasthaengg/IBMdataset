def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

N = int(input())
divisors = make_divisors(N)
ans = 0
divisors.sort(reverse=True)
for x in divisors:
    if x > 1:
        temp = x - 1
        d,m = divmod(N,temp)
        if d != m:
            break
        else:
            ans += temp
print(ans)