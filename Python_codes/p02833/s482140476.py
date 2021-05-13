n = int(input())
if n%2:
    print(0)
else:
    #2と5があれば10ができる→5の方が少ない→素因数5の数を数える
    ans = (n//5)//2
    tmp = 5
    while True:
        tmp *= 5
        if tmp > n:
            break
        ans += (n//tmp)//2
    print(ans)