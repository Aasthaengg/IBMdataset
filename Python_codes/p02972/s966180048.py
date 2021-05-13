n = int(input())
a = list(map(int, input().split()))
l = [0] * (n + 1)
ans = []
for i in range(n, 0, -1):
    cnt = 0
    for j in range(1, n // i + 1):
        cnt += l[i * j]
    if cnt % 2 != a[i - 1]:
        ans.append(i)
        l[i] = 1
print(len(ans))
print(" ".join(map(str, ans)))