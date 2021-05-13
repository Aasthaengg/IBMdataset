N = int(input())

ans = 0
for i in range(1, N+1):
    count = 0
    if i%2 is 0:
        continue
    for j in range(1, i):
        if (i/j).is_integer():
            count += 1
        if j == i-1 and count == 7:
            ans += 1
print(ans)
