def divisor(n):
    div=[]
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n / i:
                div.append(n / i)
    return div

n = int(input())
ans = len(divisor(n - 1)) - 1
for i in divisor(n):
    if i == 1:
        continue
    m = n
    while m % i == 0:
        m /= i
    if m % i == 1:
        ans += 1

print(ans)