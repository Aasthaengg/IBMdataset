n = int(input())
ans = (n+1) * (n//2) - n
if n%2 == 1:
    ans += n//2 + 1
print(ans)
