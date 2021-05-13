n, k = map(int, input().split())
s = input()
r = [0, 1]
prev = s[0]

for i in range(1, len(s)):
    if prev == s[i]:
        r[-1] += 1
    else:
        r.append(r[-1] + 1)
    prev = s[i]

lr = len(r)
import math
# 0の数よりkが大きい
if s[0] == '0' and math.ceil((lr-1) / 2) <= k:
    print(len(s))
    exit()
if s[0] == '1' and math.floor((lr-1) / 2) <= k:
    print(len(s))
    exit()

start = 0
if s[0] == '0':
    start = 1

ans = 0
for i in range(start, lr - (2 * k + 1), 2):
    ans = max(ans, r[i + (2 * k + 1)] - r[i])
    #print(i, i+(2*k)+1, r[i+(2 * k)+1] - r[i])

#print(ans)
# 0始まり
if s[0] == '0':
    ans = max(ans, r[2 * k] - r[0])
    #print(ans)
# 0終わり
if s[-1] == '0':
    ans = max(ans, r[-1] - r[lr - 2 * k - 1])
    #print(ans)
#print(r)
print(ans)

