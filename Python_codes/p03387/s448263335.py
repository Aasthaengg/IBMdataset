ABC = list(map(int, input().split()))
ABC.sort()
ans = 0

while ABC.count(min(ABC)) != 3:
    if ABC.count(min(ABC)) == 2:
        dif = ABC[2] - ABC[0]
        ABC[0] += dif
        ABC[1] += dif
        ans += dif
    else:
        ABC[0] += 2
        ans += 1
        ABC.sort()

print(ans)