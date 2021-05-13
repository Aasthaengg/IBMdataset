x = int(input())

ans = 0
yen = 100
while True:
    if yen >= x:
        print(ans)
        break
    yen = yen * 101 // 100
    ans += 1