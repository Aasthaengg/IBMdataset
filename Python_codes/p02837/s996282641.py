n = int(input())
a = []
xy = []

for i in range(n):
    a += [int(input())]
    xy += [[list(map(int,input().split())) for i in range(a[i])]]

honest = []
for i in range(2 ** n):
    flag = 0
    for j in range(n):
        if (i >> j)&1 == 1: #j番目は正直であるとき
            for person_state in xy[j]:
                if (i >> (person_state[0]-1) & 1) != person_state[1]:
                    flag = 1 #矛盾が生じるとflagを立てる
                    break
    if flag == 0:
        honest += [bin(i)[2:].count("1")]

print(max(honest))