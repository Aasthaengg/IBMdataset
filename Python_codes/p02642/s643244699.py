n = int(input())
a = list(map(int, input().split()))
a.sort()
data = [0 for _ in range(1000001)]
for x in a:
    data[x] += 1

ans = 0
for i in range(1,1000001):
    if not data[i]:continue
    if data[i] == 1:ans += 1
    j = i
    while j < 1000001:
        data[j] = 0
        j += i

print(ans)