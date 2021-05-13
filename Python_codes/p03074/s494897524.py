from itertools import accumulate
n, k = map(int, input().split())
s = input() + "_"

compressed = []

first = s[0]
prev = s[0]
cnt = 1
for x in s[1:]:
    if prev == x:
        cnt += 1
    else:
        if x == "1":
            compressed.append(cnt)
            cnt = 1
        else:
            compressed.append(cnt)
            cnt = 1
    prev = x


result = [0] + list(accumulate(compressed))

ans = []
if first == "1":
    for i in range(0, len(result), 2):
        ans.append(result[min(i + k * 2 + 1, len(result) - 1)] - result[i])
    for j in range(1, len(result), 2):
        ans.append(result[min(j + k * 2, len(result) - 1)] - result[j])
else:
    for i in range(0, len(result), 2):
        ans.append(result[min(i + k * 2, len(result) - 1)] - result[i])
    for j in range(1, len(result), 2):
        ans.append(result[min(j + k * 2 + 1, len(result) - 1)] - result[j])

print(max(ans))