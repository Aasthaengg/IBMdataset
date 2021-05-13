import collections
s = input()
cnt = collections.Counter(s)
cnt = cnt.most_common()
# print(cnt)
if len(cnt) == 1:
    if len(s) == 1:
        print('YES')
    else:
        print('NO')
    # print('YES')
    exit()
if len(cnt) == 2:
    if len(s) == 2:
        print('YES')
    else:
        print('NO')
    exit()

if cnt[0][1] > cnt[-1][1] + 1:
    print('NO')
else:
    print('YES')
