n = int(input())
ans = 0
s = 0

while s < n:
    ans += 1
    s = int(ans*1.08)
    if s == n:
        print(ans)

if s != n:
    print(":(")