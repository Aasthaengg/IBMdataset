# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_c
from collections import defaultdict

H,W = map(int,input().split())
C = defaultdict(int)
for _ in range(H):
    row = list(input())
    for i in range(W):
        C[row[i]] += 1
if H%2==0 and W%2==0:
    flag = 0
    for a in C:
        if C[a]%4!=0:
            flag = 1
            break
    if flag==0:
        print("Yes")
    else:
        print("No")
elif (H%2==0 and W%2==1) or (H%2==1 and W%2==0):
    n = (H//2)*(W//2)
    for a in C:
        if C[a]>=4:
            n -= C[a]//4
            C[a] = C[a]%4
    if n>0:
        print("No")
    else:
        flag = 0
        for a in C:
            if C[a]%2==1:
                flag=1
                break
        if flag==0:
            print("Yes")
        else:
            print("No")
else:
    n = (H//2)*(W//2)
    for a in C:
        if C[a]>=4:
            n -= C[a]//4
            C[a] = C[a]%4
    if n>0:
        print("No")
    else:
        cnt = 0
        for a in C:
            cnt += C[a]%2
        if cnt==1:
            print("Yes")
        else:
            print("No")


# 1つの行において列数が偶数の場合、例えば左端にaを置いた場合は、
# その列がpalindromeになる関係上必然的に右端にもaを置くことになる。
# さらに、列方向に見た場合は、今置いた2つのaに対して、一番下の行で
# それぞれを置く必要がある。したがって、1つのaを置くと、芋づる式に
# 合計４つのaを置くことになる。
# 行・列のどちらかが奇数の場合は、その真ん中のところにおいては
# 2個でよかったり、3個でよかったり、1個で良かったりするので、場合分けする。
