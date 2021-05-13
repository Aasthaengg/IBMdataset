#AGC016-A Shrinking
"""
毎回消去される文字は選べるもんだと思っていたら、必ず最後尾
の文字が無くなる感じだった。
出現する文字全てに対し最も長いところが答え。
"""
import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')

dic1 = defaultdict(int)
for i in s:
    dic1[i] += 1

lst1 = []
for i,j in dic1.items():
    lst1.append([j,i])
lst1.sort(reverse=True)

ans = 10**10
for i,j in lst1: #i,出現回数,j:文字
    target = j
    res = []
    res2 = 0
    for k in s:
        if k==target:
            res.append(res2)
            res2 = 0
        else:
            res2+=1
    res.append(res2)
    ans_res = max(res)
    ans = min(ans,ans_res)

print(ans)