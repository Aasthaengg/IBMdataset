
n = int(input())
a = list(map(int, input().split()))
flags = [False] * n
ans = 0
for i in range(n):
    if a[a[i] - 1] - 1 == i and flags[a[i] - 1] == False:
        ans += 1
        flags[a[a[i] - 1] - 1] = True

print(ans)