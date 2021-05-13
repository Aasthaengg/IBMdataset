k, a, b = map(int, input().split())

if b-a <= 2:
    print(1+k)
    exit()
    
check = 0
ans = 1

while True:
    if check == 0:
        if (k-2) >= a-1:
            k = k-2-(a-1)
            ans -= 1
            ans += b
            check = 1
            continue
        else:
            ans += k
            break
    else:
        if k % 2 == 0:
            s = k//2
            ans -= a * s
            ans += b * s
        else:
            s = k//2
            ans -= a * s
            ans += b * s + 1
    break

print(ans)