x = int(input())
yen = 100
ans = 0

while x > yen:
    yen += yen//100
    ans += 1

print(ans)
