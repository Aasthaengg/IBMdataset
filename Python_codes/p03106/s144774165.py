def Div(N):
    L = []
    R = []
    I = 1
    while I*I<=N:
        if N%I==0:
            L.append(I)
            if I!=N//I: R.append(N//I)
        I += 1
    return R+L[::-1]
  
A,B,K = (int(X) for X in input().split())
Count = 0
Divid = Div(min(A,B))
for T in Divid:
    if A%T==0 and B%T==0:
        Count += 1
        if Count==K:
            print(T)
            break