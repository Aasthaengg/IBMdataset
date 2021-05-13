N, M = list(map(int,input().split()))
K_and_Ss = []
for i in range(M):
    data = list(map(int,input().split()))
    K_and_Ss.append(data)
Ps = list(map(int,input().split()))

flag = False
x = 2**N
sum = 0
for i in range(x):
    for j in range(M): #j番目の電球がついているかを判定
        count = 0
        if flag:
            flag = False
            break
        for k in range(len(K_and_Ss[j])-1):
            if (i >> (K_and_Ss[j][k+1]-1) & 1) == 1:
                count += 1
            if k ==len(K_and_Ss[j])-2 and count % 2 == Ps[j]:
                flag = False
                if j == M-1:
                    sum += 1
            if k ==len(K_and_Ss[j])-2 and count % 2 != Ps[j] and j != M-1:
                flag = True
print(sum)
