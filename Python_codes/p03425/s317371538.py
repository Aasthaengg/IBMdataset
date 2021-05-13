# abc089c
import itertools
import sys
n = int(input())
s = [input() for i in range(n)]
'''
1.
M,A,R,C,Hから始まる名前を抽出する
2.
MARCHの5文字から3文字選ぶ
3.
選んだ文字ごとに、人数の掛け算を行う
'''
m = 0
a = 0
r = 0
c = 0
h = 0
for si in s:
    if si[0] == 'M':
        m += 1
    elif si[0] == 'A':
        a += 1
    elif si[0] == 'R':
        r += 1
    elif si[0] == 'C':
        c += 1
    elif si[0] == 'H':
        h += 1
if m == 0 and a == 0 and r == 0 and c == 0 and h == 0:
    print(0)
else:
    p = itertools.combinations(['M','A','R','C','H'], 3)
    ans = 0
    for i in p:
        ans_ = 1
        if 'M' in i:
            ans_ *= m
        if 'A' in i:
            ans_ *= a
        if 'R' in i:
            ans_ *= r
        if 'C' in i:
            ans_ *= c
        if 'H' in i:
            ans_ *= h
        ans += ans_
    print(ans)