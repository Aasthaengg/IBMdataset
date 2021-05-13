#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

a,b,c,d,e,f = map(int, input().split())

#まず容器fグラムに入る分の砂糖の組み合わせを考える。
suger = []
for i in range(0, f+1):
    for j in range(0, f+1):
        tmp = c*i + d*j
        if (tmp <= f):
            suger.append(tmp)
suger = list(set(suger))

#次に容器fグラムに入る分の水の組み合わせを考える
watter = []
for i in range(0, f+1, 100):
    for j in range(0, f+1, 100):
        tmp = (a*i + b*j)
        if (tmp <= f):
            watter.append(tmp)

watter = list(set(watter))

#sugerとwatterの組み合わせを列挙して、条件を満たすもので濃度を列挙する
max_conset = -1.0
ans_watter = 0
ans_sugger = 0

#print(watter)
#print(suger)

for i in range(len(watter)):
    for j in range(len(suger)):

        if (0 < suger[j] + watter[i] <= f):
            if (watter[i] // 100 * e >= suger[j]):
                consent = 100 * suger[j] / (watter[i] + suger[j])
                if (max_conset < consent):
                    ans_watter = watter[i] + suger[j]
                    ans_sugger = suger[j]
                    max_conset = consent

print(ans_watter, ans_sugger)


