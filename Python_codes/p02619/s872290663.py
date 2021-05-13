d = int(input())
cs = list(map(int, input().split()))
sm = [list(map(int, input().split())) for _ in range(d)]
ts = [int(input()) for _ in range(d)]
ls = [0] * 26

s = 0
for i in range(d):
    t = ts[i]
    t -= 1
    s += sm[i][t]
    ls[t] = i + 1
    #print('contest',t+1)
    #print('plus',sm[i][t])
    #print(ls)
    #print(cs)

    dis = sum(c * ((i+1) - l) for c, l in zip(cs, ls))
    #print('dis',dis)
    s -= dis

    print(s)
