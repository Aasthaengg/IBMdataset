N = int(input())

if N%2:
    ans = 0
else:
    ans = 0
    d = 10
    while d <= N:
        ans += N//d
        d *= 5

print(ans)
