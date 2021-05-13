import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


from collections import defaultdict

N = I()
D = LI()
d1 = defaultdict(int)  # 問題案
for d in D:
    d1[d] += 1

M = I()
T = LI()
d2 = defaultdict(int)  # 必要な問題
for t in T:
    d2[t] += 1

for key in d2.keys():
    if d2[key] > d1[key]:
        print('NO')
        break
else:
    print('YES')
