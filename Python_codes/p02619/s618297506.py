D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

socre = 0
his = [0] * len(C)

for i in range(D):
    t = int(input())
    t -= 1
    his[t] = i + 1
    sat = 0
    for j in range(len(C)):
        sat += C[j] * (i - his[j] + 1)
    socre += S[i][t] - sat

    print(socre)