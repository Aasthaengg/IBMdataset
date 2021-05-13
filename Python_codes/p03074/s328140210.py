n, k = map(int, input().split())
s = input()

l_01 = []
l_10 = []
if s[0] == '1':
    l_01.append(0)
for i in range(n-1):
    if s[i] == '0' and s[i+1] == '1':
        l_01.append(i+1)
    elif s[i] == '1' and s[i+1] == '0':
        l_10.append(i+1)
if s[-1] == '1':
    l_10.append(n)

cnt_0 = len(l_01) - 1
if s[0] == '0':
    cnt_0 += 1
if s[-1] == '0':
    cnt_0 += 1
cnt_1 = len(l_01)

if k >= cnt_0:
    print(n)
else:
    res = 0
    i = 0
    while i + k < cnt_1:
        res = max(res, l_10[i+k] - l_01[i])
        i += 1
    if s[0] == '0':
        res = max(res, l_10[k-1])
    if s[-1] == '0':
        res = max(res, n - l_01[-k])
    print(res)