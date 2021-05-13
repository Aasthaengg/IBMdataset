N = int(input())
a = list(map(int, input().split()))
pair = {}
ans = 0
for i in range(N):
    pair[i + 1] = a[i]

for key, value in pair.items():
    if pair[value] == key:
        ans += 1

print(ans // 2)
