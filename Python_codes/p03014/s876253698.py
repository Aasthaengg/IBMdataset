h,w=map(int,input().split())

M=[]
for i in range(h):
    M.append(input())

L=[]
for j in range(h):
    Lj=[]
    for i in range(w):
        if M[j][i]=="#":
            Lj.append(0)
        elif i==0:
            Lj.append(1)
        else:
            Lj.append(Lj[i-1]+1)
    L.append(Lj)
R=[]
for j in range(h):
    Rj=[]
    for i in range(w):
        if M[j][w-1-i]=="#":
            Rj.append(0)
        elif i==0:
            Rj.append(1)
        else:
            Rj.append(Rj[i-1]+1)
    R.append(Rj)   
U=[]
for i in range(w):
    Ui=[]
    for j in range(h):
        if M[j][i]=="#":
            Ui.append(0)
        elif j==0:
            Ui.append(1)
        else:
            Ui.append(Ui[j-1]+1)
    U.append(Ui)
D=[]
for i in range(w):
    Di=[]
    for j in range(h):
        if M[h-1-j][i]=="#":
            Di.append(0)
        elif j==0:
            Di.append(1)
        else:
            Di.append(Di[j-1]+1)
    D.append(Di)

s=0
for i in range(w):
    for j in range(h):
        s=max(s,L[j][i]+R[j][w-1-i]+U[i][j]+D[i][h-1-j]-3)

print(s)