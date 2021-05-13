n,m=map(int,input().split())
k=[list(map(int,input().split())) for _ in range(m)]
p=list(map(int,input().split()))

answer = 0
switch = []
for i in range(2 ** n):
    _switch = [0] * n
    for j in range(n):

        if i >> j & 1 :
            _switch[j]  = 1
    switch.append(_switch)

for i in range(2 ** n):
    flag = True
    for j in range(m):
        light = 0
        for _k  in k[j][1:]:
            light += switch[i][_k - 1]

        if light % 2 != p[j]:
            flag = False

    if flag:
        answer += 1

print(answer)