n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab = sorted(ab, key=lambda x:(x[1],-x[1]))

total = 0
for a, b in ab:
    total += a
    if total <= b:
        continue
    else:
        print("No")
        exit()
else:
    print("Yes")