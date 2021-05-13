n = int(input())

ans = n+1-2
for i in range(1, round(n**0.5)+1):
    if n%i == 0:
        x = n//i + i - 2

        if x < ans:
            ans = x

print(ans)