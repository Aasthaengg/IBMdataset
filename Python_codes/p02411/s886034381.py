'''
先に基準を変数で設定して、whileで回すと見た目もきれいだし、あとから調整も楽。
ついでだからclass化する？しなくてもいいけど。
while意味ない
'''
s = []

while True:
    t = input()
    if t == "-1 -1 -1":
        break
    else:
        s.append(list(map(int, t.split())))
        
#print(r)

#テスト値。リストにしておかないとインプットがうまくいかなくなるはず。
#s = [[20,20,40],[40,40,-1],[-1,50,60]]

#80,65,50,30
a, b, c, d = 80, 65, 50, 30

g = []

for i in range(len(s)):
    r = s[i][0] + s[i][1]
    
    if s[i][0]==-1 or s[i][1]==-1:
        g.append("F")
        #break
    elif r >= a:
        g.append("A")
    elif r >= b:
        g.append("B")
    elif r >= c:
        g.append("C")
    elif r >= d:
        if s[i][2] >= 50:
            g.append("C")
        else:
            g.append("D")
    else:
        g.append("F")
    
[print(g[i]) for i in range(len(g))]

    
