mod = 1000000007

N = int(input())

pos = []
neg = []
zer = []
inf = []
sol = 0

###除外すべき組み合わせの個数を数える
NG = []

for i in range(N):
    a,b = map(int,input().split())
    if a*b > 0:
        pos.append((abs(a),abs(b)))
    elif a*b < 0:
        neg.append((-abs(a),abs(b)))
    elif a == 0 and b != 0:
        inf.append((0,b))
    elif a != 0 and b == 0:
        zer.append((a,0))
    else:
        sol += 1

NG.append((len(inf),len(zer)))
free = len(pos)+len(neg)


# 以下しばらくneg,posに含まれるものに関する議論

pos.sort(key=lambda x:(x[1]/x[0]))
neg.sort(key=lambda x:(x[1]/x[0]))

x = 0
y = 0


while (x < len(pos) and y < len(neg)):
    if pos[x][0]*neg[y][0]+pos[x][1]*neg[y][1] == 0:
        s = 1
        t = 1
        while x+1 < len(pos) and pos[x+1][0]*neg[y][0]+pos[x+1][1]*neg[y][1] == 0:
            x += 1
            s += 1
        while y+1 < len(neg) and pos[x][0]*neg[y+1][0]+pos[x][1]*neg[y+1][1] == 0:
            y += 1
            t += 1
        NG.append((s,t))
        x += 1
        y += 1
        free -= (s+t)
        continue


    if x >= len(pos)-1 and y >= len(neg)-1:
        break

    elif y+1 < len(neg) and pos[x][0]*neg[y][0]+pos[x][1]*neg[y][1] > 0:
        y += 1
    elif x+1 < len(pos) and pos[x][0]*neg[y][0]+pos[x][1]*neg[y][1] < 0:
        x += 1
    elif x >= len(pos)-1:
        y += 1
    elif y >= len(neg)-1:
        x += 1

ans = pow(2,free,mod)

for s,t in NG:
    # s個のうち1個以上入れる or t個のうち1個以上入れる or どちらも1つも入れない
    ans *= pow(2,s,mod)-1 +pow(2,t,mod)-1 +1
    ans %= mod

#print('free',free)
#print('NG',NG)

# 1つも選ばないものの除外、solは単体で選べばOK
print((ans+sol-1)%mod)

