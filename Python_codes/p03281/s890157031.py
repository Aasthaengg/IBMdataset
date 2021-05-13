n = int(input())

ans = 0
sqrt = 1

for i in range(1,n+1,2):
    if i == sqrt*sqrt:
        sqrt += 1
        continue
    elif i > sqrt*sqrt:
        sqrt += 1
    count = 0
    for j in range(1,sqrt,2):
        if i%j == 0:
            count += 1
    if count == 4:
        ans += 1

print(ans)
