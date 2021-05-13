import copy

n = int(input())
a = list(map(int,(input().split())))
s = [0]*n
s[0] = a[0]
for i in range(n-1):
    s[i+1] = s[i] + a[i+1]

s2 = copy.copy(s)
ans = []

# 最初を正とする場合
ans1 = 0
tmp = 0
for i in range(n):
    if i%2 == 0: #奇数項
        s[i] += tmp
        if s[i] <= 0:
            tmp += 1 - s[i]
            ans1 += 1 - s[i]
    else: #偶数項
        s[i] += tmp
        if s[i] >= 0:
            tmp -= s[i] + 1
            ans1 += s[i] + 1

s = s2
# 最初を負とする場合
ans2 = 0
tmp = 0
for i in range(n):
    if i%2 == 0: #奇数項
        s[i] += tmp
        if s[i] >= 0:
            tmp -= s[i] + 1
            ans2 += s[i] + 1
    else: #偶数項
        s[i] += tmp
        if s[i] <= 0:
            tmp += 1 - s[i]
            ans2 += 1 - s[i]

print(min(ans1,ans2))