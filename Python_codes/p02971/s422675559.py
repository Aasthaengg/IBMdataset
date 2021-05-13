N = int(input())
A = []
dicA = {}

for i in range(N):
    tmp = int(input())
    dicA[tmp] = dicA.get(tmp, 0) + 1
    A.append(tmp)

sortA = sorted(dicA.items(), key=lambda x: x[0], reverse=True)

for ai in A:
    if ai != sortA[0][0] or sortA[0][1] != 1:
        print(sortA[0][0])
    else:
        print(sortA[1][0])