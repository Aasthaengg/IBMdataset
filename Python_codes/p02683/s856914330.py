import itertools
N,M,X = map(int,input().split())
L = [i for i in range(0,2)]
c_list = list(itertools.product(L, repeat=N)) #重複あり組み合わせ
Alg = []
for i in range(N):
    Alg.append(list(map(int,input().split())))
Ans = 1<<50
Money = 0
def judge(per):
    Money = 0
    tryAlg = [0]*M
    for i in range(len(per)):
        if per[i] == 1:
            Money += Alg[i][0]
            for j in range(1,M+1):
                tryAlg[j-1] += Alg[i][j]
    for m in tryAlg:
        if m < X:
            Money = -1
            break
    return Money
for per in c_list:
    An = judge(per)
    if An != -1:
        Ans  = min(An,Ans)
if Ans == 1<<50:
    Ans = -1
print(Ans)