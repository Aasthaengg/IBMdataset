n = int(input())
ans = [0] * 10050

for x in range(1, 105):
    for y in range(1, 105):
        for z in range(1, 105):
            zzz = (x + y + z) ** 2 - x * y - y * z - x * z
            if zzz < 10050:
                ans[zzz] += 1

for i in range(n):
    print(ans[i+1])
