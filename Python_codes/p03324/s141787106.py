d, n = [int(x) for x in input().split()]
gap = 100 ** d
gap_check = gap * 100
count = 0
ans = 0
while True:
    ans += gap
    if ans % gap_check != 0:
        count += 1
        if count >= n:
            break
print(ans)