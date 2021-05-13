#一昨日(a),昨日(b),今日(c)のペンキの色
a,b,c = input().split()
#買ったペンキの数
S = 1
#aとbが違う色か
if not a == b:
    S = S + 1
#aとc、かつbとcが違う色か
if not a == c and not b == c:
    S = S + 1
#買ったペンキの数を出力
print(S)