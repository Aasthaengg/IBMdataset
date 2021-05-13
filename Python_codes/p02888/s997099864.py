#D - Triangles

N = input()
N = int(N)
L = list(map(int,input().split()))

L_sorted = sorted(L, reverse = False)#昇順

def judge(A,B,x):#cが三角形になるか判定する関数
    if A + B <= L_sorted[x]:#a + b = cの時はfinを持ってくる
        return 'high'
    else :
        return 'low'

count = 0
for i in range(N):#aの選び方
    for j in range(i+1,N):#bの選び方
        a = L_sorted[i]
        b = L_sorted[j]#b <= c < a+b
        sta = 0
        fin = N#Lの個数+1
        while fin > sta + 1:#cの選び方
            m = ((fin - sta) // 2) + sta
            if judge(a,b,m) == 'high':
                fin = m
            elif judge(a,b,m) == 'low':
                sta = m
        count += sta  - j    
print(count)