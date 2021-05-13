n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if i + 1 == a[a[i] - 1] and i < a[i]:
        cnt += 1
print(cnt)
