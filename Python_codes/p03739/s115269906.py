n = int(input())
alst = list(map(int, input().split()))
ans = []
for pm in range(2):
    total = 0
    tmp = 0
    for j, num in enumerate(alst):
        total += num
        if (j + pm) % 2 == 0:
            if total > 0:
                pass
            else:
                tmp += abs(1 - total)
                total = 1
        else:
            if total < 0:
                pass
            else:
                tmp += abs(-1 - total)
                total = -1
    ans.append(tmp)
print(min(ans))