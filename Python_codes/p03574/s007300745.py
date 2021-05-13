h,w=map(int,input().split())
c=["."+input()+"." for i in range(h)]
s=["."*(w+2)]
s.extend(c)
b=["."*(w+2)]
s.extend(b)
sc=[[0for _ in range(w+2)] for i in range(h+2)]
# print(sc)

for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j]=="#":
            if sc[i-1][j-1]!="#":
                sc[i-1][j-1]+=1
            if sc[i][j-1]!="#":
                sc[i][j-1]+=1
            if sc[i+1][j-1]!="#":
                sc[i+1][j-1]+=1
            if sc[i-1][j]!="#":
                sc[i-1][j]+=1
            if sc[i+1][j]!="#":
                sc[i+1][j]+=1
            if sc[i-1][j+1]!="#":
                sc[i-1][j+1]+=1
            if sc[i][j+1]!="#":
                sc[i][j+1]+=1
            if sc[i+1][j+1]!="#":
                sc[i+1][j+1]+=1
            sc[i][j]="#"
for i in range(1,h+1):
    ne="".join([str(_) for _ in sc[i]])
    ne=ne[1:w+1]
    print(ne)