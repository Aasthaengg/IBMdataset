#C-HandV
import copy
ans = 0
S = []
S_red = []
S_kuro = []
H_parameter = [[0]]
W_parameter = [[0]]
Hsize = 0
Wsize = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

#入力
H,W,K   = map(int, input().split())
for i in range(H):
    S.append(list(map(str, input())))

#red操作
#H
for n1 in range(1,H+1,1):
    H_parameter.append([n1])
    for n2 in range(1,H+1,1):
        if n2 > n1:
            H_parameter.append([n1,n2])
            for n3 in range(1,H+1,1):
                if n3 > n2:
                    H_parameter.append([n1,n2,n3])
                    for n4 in range(1,H+1,1):
                        if n4 > n3:
                            H_parameter.append([n1,n2,n3,n4])
                            for n5 in range(1,H+1,1):
                                if n5 > n4:
                                    H_parameter.append([n1,n2,n3,n4,n5])
                                    for n6 in range(1,H+1,1):
                                        if n6 > n5:
                                            H_parameter.append([n1,n2,n3,n4,n5,n6])
Hsize = len(H_parameter)
#print(H_parameter)
#print(Hsize)

#W
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

for n1 in range(1,W+1,1):
    W_parameter.append([n1])
    for n2 in range(1,W+1,1):
        if n2 > n1:
            W_parameter.append([n1,n2])
            for n3 in range(1,W+1,1):
                if n3 > n2:
                    W_parameter.append([n1,n2,n3])
                    for n4 in range(1,W+1,1):
                        if n4 > n3:
                            W_parameter.append([n1,n2,n3,n4])
                            for n5 in range(1,W+1,1):
                                if n5 > n4:
                                    W_parameter.append([n1,n2,n3,n4,n5])
                                    for n6 in range(1,W+1,1):
                                        if n6 > n5:
                                            W_parameter.append([n1,n2,n3,n4,n5,n6])
Wsize = len(W_parameter)
#print(W_parameter)
#rint(Wsize)
Qcount = 0

for l in range(Hsize):
    ll = len(H_parameter[l])
    for m in range(Wsize):
        S_red.clear()
        S_red = copy.deepcopy(S)
        mm = len(W_parameter[m])
        for q in range(ll):
            for r in range(mm):
                if H_parameter[l] != [0]:
                    for p in range(W):
                        S_red[H_parameter[l][q]-1][p]= 'R'
                if W_parameter[m] != [0]:            
                    for s in range(H):
                        S_red[s][W_parameter[m][r]-1]= 'R'
                
        # 黒の数
        Q = 0
        Qcount += 1
        S_kuro.clear()
        for j in range(H):
            for k in range(W):
                S_kuro.append(S_red[j][k])
        Q =S_kuro.count('#')
        #print(l,m,Q)
        #print(S_kuro)          
        if Q == K : ans += 1

# 出力
print(ans)