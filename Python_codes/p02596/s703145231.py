k = int(input())
ans = -1
prev = 0
for i in range(1, k + 1):
    prev = (10 * prev + 7) % k
    if prev == 0:
        ans = i
        break
print(ans)