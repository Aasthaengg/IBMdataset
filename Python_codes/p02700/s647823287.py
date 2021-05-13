a, b, c, d = list(map(int, input().split()))
c -= b
ans = "No"
while True:
    a -= d
    if c <= 0:
        ans = "Yes"
        break

    c -= b
    if a <= 0:
        break

print(ans)