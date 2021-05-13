n = int(input())
    
def md(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

a = md(n)

ans = 0
for i in a:
    b = n // i
    if i < b-1:
        ans += (b-1)
        
print(ans)