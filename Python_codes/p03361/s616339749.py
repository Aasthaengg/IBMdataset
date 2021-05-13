H,W=map(int,input().split())
S=["."*(W+2)]
for _ in range(H):
    S.append("."+input()+".")
S.append("."*(W+2))

G=True
V=[(-1,0),(1,0),(0,-1),(0,1)]
for y in range(H+2):
    for x in range(W+2):
        if S[y][x]=="#":
            F=False
            for (a,b) in V:
                F|=(S[y+b][x+a]=="#")

            G&=F

if G:
    print("Yes")
else:
    print("No")
