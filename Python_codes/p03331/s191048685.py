n = int(input())
if n % 10 == 0:
    print(10)
else:
    ans = 0
    for s in str(n):
        ans += int(s)
    print(ans)
