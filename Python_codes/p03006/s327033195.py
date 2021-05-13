import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(readline())
lst1 = [list(map(int,readline().split())) for i in range(n)]
lst1.sort()
cost = 1
if n == 1:
    print(cost)
    exit()
#同じベクトルでつなげる要素を最大化する。全点対象にベクトルを求め、多数決。
dic1 = dict()

for i in range(n-1):
    for j in range(i+1,n):
        x,y = lst1[i][0] - lst1[j][0] , lst1[i][1] - lst1[j][1]
        """
        if x < 0 and y < 0:
            x,y = -x,-y
        elif x < 0 and y >= 0:
            x,y = -x,-y"""
        if (x,y) in dic1:
            dic1[(x,y)] += 1
        else:
            dic1[(x,y)] = 1

#線分は頂点-1個。そのうち同ベクトル数が免除される。
cost += n-1
cost -= max(dic1.values())

print(cost)