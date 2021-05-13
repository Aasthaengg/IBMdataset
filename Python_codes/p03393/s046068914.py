# https://atcoder.jp/contests/agc022/tasks/agc022_a

from string import ascii_lowercase

s = input()
rems = [c for c in ascii_lowercase if c not in s]

if len(rems) > 0:
    print("{}{}".format(s, rems[0]))
    exit()
else:
    # 長さ26文字
    # S = [p1, ..., p26]

    # 右から見て照準である最長な文字列を探す
    j = len(s) - 1
    while s[j] < s[j - 1]:
        j -= 1

    if j == 0:
        print(-1)
    else:
        sj = s[:j - 1]
        pjm1 = s[j - 1]
        nc = min([c for c in s[j:] if c > pjm1])
        print(sj + nc)