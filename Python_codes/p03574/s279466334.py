h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(input())
S=[]
for i in range(h):
    S.append([])
x=[-1,-1,-1,0,0,1,1,1]
y=[-1,0,1,-1,1,-1,0,1]
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            t=0
            for k in range(8):
                if 0<=i+x[k]<h and 0<=j+y[k]<w and s[i+x[k]][j+y[k]]=="#":
                    t+=1
            T=str(t)
            S[i].append(T)
        else:
            S[i].append("#")
for i in range(h):
    print("".join(S[i]))