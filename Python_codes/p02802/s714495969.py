#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n,m = map(int, input().split())
p = [list(map(str,input().split())) for i in range(m)]

#コンテスト毎に["AC","WA","AC"]を格納する
d = {}

for i in range(m):
    key = p[i][0]
    val = p[i][1]
    if key in d:
        d[key].append(val)
    else:
        d[key] = [val]

# AC数を求める
acNum = 0

for v in d.values():
    if "AC" in v:
        acNum += 1

# WA数求める
waNum = 0

for v in d.values():
    if "AC" in v:
        for i in range(len(v)):
            if v[i] == "AC":
                break
            else:
                waNum += 1
print(acNum, waNum)

