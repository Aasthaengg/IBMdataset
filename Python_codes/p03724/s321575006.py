"""
rootを決めて、aから必ずrootを通ってbに到達するとする
aとbのlcaより上は、+2されることになるので、実質通っていないのと同値
どんな木であっても、自分自身が偶数回(0を含む)でてこないと
ノードの値は偶数にはなりえない
"""
n, m = map(int, input().split())
cnts = [0] * (n+1) 
for i in range(m):
    a,b = map(int, input().split())
    cnts[a] += 1
    cnts[b] += 1
if all([c%2 == 0 for c in cnts]):
    print("YES")
else:
    print("NO")