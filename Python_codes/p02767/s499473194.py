#C - Rally
N = int(input())
X = list(map(int, input().split()))

P_list = []
for P in range(1, max(X)+1):
    P_list.append(P)

HP_min =10**8#取りうるHPの最大値    
for i in range(len(P_list)):#Pに関する繰り返し
    HP = 0
    for j in range(N):#Xに関する繰り返し
        HP += (X[j] - P_list[i])**2#Pごとに終わらせたい
    #あるPに対しての処理 
    if HP < HP_min:
        HP_min = HP
print(HP_min)