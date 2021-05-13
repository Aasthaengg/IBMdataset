from collections import deque

N, K = map(int, input().split(' '))
S = input()
arr = []
idx = 0

while idx < N:
    start = idx
    while idx + 1 < N and S[idx] == S[idx + 1]:
        idx += 1
    if S[start] == '0':
        arr.append(-(idx - start + 1))
    else:
        arr.append(idx - start + 1)
    idx += 1

if arr[0] < 0:
    arr = [0] + arr
if arr[-1] > 0:
    arr.append(0)

l, r = 0, 0     # [l, r)
ans, tmp = max(arr), 0
while l < len(arr) and r < len(arr):
    tmp += abs(arr[r])
    r += 1

    if r - l > 2 * K + 1:
        tmp -= arr[l] - arr[l + 1]
        l += 2

    if r - l <= 2 * K + 1:
        ans = max(ans, tmp)
print(ans)