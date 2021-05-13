x = int(input())
ans = 0
for b in range(1, 32): # 1000**0.5より31
    for p in range(2, 10): # log2(1000)より9
        tmp = b**p
        if tmp <= x and tmp >= ans:
            ans = tmp
print(ans)