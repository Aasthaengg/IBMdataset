#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n,m = map(int, input().split())
l = [list(map(int,input().split())) for i in range(m)]

# n,mが10^5なのでO(n^2)は間に合わない
"""
ans = 0
for i in range(1,n+1):
    flg = True
    for j in range(m):
        if i < l[j][0] or i > l[j][1]:
            flg = False
    if (flg):
        ans+=1
print(ans)
"""

#lをO(m)で走査して上限、下限をあらかじめ確定しておく
up = 10**5+1
lo = 0

for i in range(m):
    if lo < l[i][0]:
        lo = l[i][0]
    if  up > l[i][1]:
        up = l[i][1]

"""
#わざわざ回す必要がない
ans = 0
for i in range(1,n+1):
    if i >= lo and i <= up:
        ans+=1
"""
if (up - lo >= 0):
    print(up -lo+1)
else:
    print(0)


