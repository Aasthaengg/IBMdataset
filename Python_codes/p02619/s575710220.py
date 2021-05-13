D = int(input())
C = [*map(int, input().split())]
S = [[*map(int, input().split())] for _ in range(D)]
T = [int(input()) for _ in range(D)]

# print(D)
# print(C)
# print(*S,sep='\n')
# print(T)

O = [[0]*26 for _ in range(D)]
A = [[0]*26 for _ in range(D)]

def last(d,t):
    for i in range(d,-1,-1):
        if O[i][t] > 0: return i+1
    return 0

score = 0
t = 0
for d in range(D):
    t = T[d] - 1
    # print('t',t)
    O[d][t] = 1
    # print(O)
    dw = 0
    for i in range(26):
        # print('lday',last(d,i))
        dw += C[i]*((d+1) - last(d,i))
    A[d][t] = S[d][t] - dw
    score += A[d][t]
    # print(t+1,end=' ')
    # print(S[d][t],end=' ')
    # print(dw,end=' ')
    print(score)
    # t = (t+1) % 26

