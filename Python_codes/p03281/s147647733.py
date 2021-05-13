def Div(N):
    L = []
    R = []
    I = 1
    while I*I<=N:
        if N%I==0:
            L.append(I)
            if I!=(N//I):
                R.append(N//I)
        I += 1
    return L+R[::-1]

N = int(input())
Count = 0
for T in range(1,N+1,2):
    if len(Div(T))==8:
        Count += 1
print(Count)