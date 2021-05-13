N, M = map(int, input().split()) # Nはスイッチの数、Mは電球の数
lights = [[0] * N for _ in range(M)]
for i in range(M): 
    temp = list(map(int, input().split())) # 0番目はスイッチの個数、1番目以降はスイッチを示す
    k = temp[0]
    switches = temp[1:]
    for j in range(k):
        lights[i][switches[j]-1] = 1
P = list(map(int, input().split())) # 個数を2で割ったあまりが要素と等しい場合に点灯する

answer_count = 0
for i in range(2**N):
    flag = True
    for k in range(M):
        count = 0
        for j in range(N):
            if (i >> j) & 1:
                count += lights[k][j]
        if count % 2 != P[k]:
            flag = False
            break
    if flag:
        answer_count += 1

print(answer_count)