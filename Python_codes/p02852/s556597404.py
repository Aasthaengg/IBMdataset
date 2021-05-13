n, m = map(int, input().split())
s = input()

dp = [float('inf')] * (n + 1)
dp[0] = 0

N = n + 1
N0 = 2 ** (N - 1).bit_length()
data = [float('inf')] * (2 * N0)

# a_k の値を x に更新
def update(k, x):
    k += N0 - 1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = min(data[2 * k + 1], data[2 * k + 2])

# [a_l, a_(l+1), ..., a_(r-1)]の最小値を求める
def query(l, r):
    L = l + N0
    R = r + N0
    s = float('inf')
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R - 1])

        if L & 1:
            s = min(s, data[L - 1])
            L += 1
        L >>= 1
        R >>= 1
    return s

update(0, 0)
for i in range(1, n + 1):
    if s[i] == '1':
        continue

    dp[i] = query(max(0, i - m), i) + 1
    update(i, dp[i])

if dp[-1] == float('inf'):
    print(-1)
else:
    cur = n
    target = dp[n] - 1
    arr = [n]

    while cur > 0:
        for i in range(max(0, cur - m), cur):
            if dp[i] == target:
                cur = i
                target -= 1
                arr.append(i)
                break

    arr = arr[::-1]
    ans = []
    for i in range(len(arr) - 1):
        ans.append(arr[i+1] - arr[i])

    for _ans in ans:
        print(_ans)
