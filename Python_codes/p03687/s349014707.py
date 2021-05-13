import collections
s = input()
ss = set(s)
# print(ss)
ans = float('inf')
# cs = collections.Counter(s)
for c in ss:
    cnt = 0
    back = 0
    # print(c)
    for si in s:
        if c != si:
            cnt += 1
        else:
            back = max(back, cnt)
            cnt = 0
    back = max(back, cnt)
    ans = min(ans, back)
    # print(ans, back)
print(ans)
# for i in cs:
#     print(i)
