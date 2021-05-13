# 2020/07/26
# AtCoder Beginner Contest 153 - C

# Input
n, k = map(int,input().split())
h = list(map(int,input().split()))

# 降順にソート
h.sort()
h.reverse()
ans = 0

for i in range(n):
    # K回まで必殺技を使う
    if i < k:
        continue
    else:
        ans = ans + h[i]

# Output
print(ans)
