a, b = map(int, input().split())
count_takahashi = 0
for month in range(1, a + 1):
    if month != a:
        count_takahashi += 1
    else:
        if b >= month:
            count_takahashi += 1

print(count_takahashi)