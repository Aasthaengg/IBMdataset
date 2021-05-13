short = 10
ans = 0
for i in range(5):
    n = int(input())
    if short > n%10 and n%10 > 0:
        short = n%10
    ans += (n//10)*10
    if n%10 > 0:
        ans += 10
ans -= 10 if short > 0 else 0
print(ans+short)
