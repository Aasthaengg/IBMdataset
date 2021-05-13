k = int(input())
mod = 7 % k
if k % 2 == 0:
    print(-1)
else:
    ans = 1
    while mod != 0:
        mod = (10*mod + 7) % k
        ans += 1
        if ans >= 10**7:
            print(-1)
            break
    if ans < 10**7:
        print(ans)