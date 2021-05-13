import math

n = int(input())
koch = [(0.0, 0.0), (100.0, 0.0)]
SIN60 = math.sin(math.radians(60))

for i in range(n):
    nextKoch = []
    for j in range(len(koch) - 1):
        p1 = koch[j]
        p2 = koch[j+1]
        # s, t は p1, p2 を 3 等分する点
        s = ((p1[0] * 2 + p2[0]) / 3, (p1[1] * 2 + p2[1]) / 3)
        t = ((p1[0] + p2[0] * 2) / 3, (p1[1] + p2[1] * 2) / 3)
        # u は s を中心として  t を 60ª 回転させた点
        ux = (t[0]-s[0])/2 - (t[1]-s[1])*SIN60 + s[0]
        uy = (t[0]-s[0])*SIN60 + (t[1]-s[1])/2 + s[1]
        u = (ux, uy)
        nextKoch[len(nextKoch):len(nextKoch)] = [p1, s, u, t]
    nextKoch.append(koch[-1])
    koch = nextKoch

for i in range(len(koch)):
    print('{0:.8f} {1:.8f}'.format(koch[i][0], koch[i][1]))

