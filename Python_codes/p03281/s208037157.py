n = int(input())
ans = 0


def divisors(n):
    set_div = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            set_div.add(i)
            set_div.add(n//i)
    return set_div


for i in range(1, n+1, 2):
    t = len(divisors(i))
    if t == 8:
        ans += 1
print(ans)
