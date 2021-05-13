#AGC034-B ABC
"""
ABC→BCA
ABCBC→BCABC→BCBCA
AABC→ABCA→BCAA

"BC"の文字列は絶対に不変で、これが"A"を左から右にキャリーする役割を持つ。
それ以外の文字列、Bの後にCが無い状態もしくは、Cの前にBが無い時、キャリーが終わる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

s = readline().rstrip().decode('utf-8')
ans = 0 
a_ct = 0
bc_ct = 0
flag = 0
for i in range(len(s)-1):
    if flag:
        flag = 0
        continue
    if s[i] == "A":
        a_ct += 1
    elif s[i] == "B":
        if s[i+1] == "C":
            bc_ct += 1
            ans += a_ct
            flag = 1
        else:
            a_ct = 0
            bc_ct = 0
    else:
        a_ct = 0
        bc_ct = 0

print(ans)