N = int(input())
res = 0
for num in range(1, N + 1):
    if num % 2 == 1:
        cnt = 0
        for d in range(1, num + 1):
            if num % d == 0:
                cnt += 1
                if cnt > 8:
                    break
        if cnt == 8:
            res += 1
print(res)
