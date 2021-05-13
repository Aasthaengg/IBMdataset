h,w=map(int,input().split())
s=[input() for i in range(h)]
for i in range(h):
    s[i]=[t.replace(".","0") for t in s[i]]
    s[i]=[t.replace("#","-9") for t in s[i]]
    s[i]=[int(t) for t in s[i]]
for i in range(h):
    for j in range(w):
        if s[i][j]<0:
            if i>0:
                s[i-1][j]+=1
                if j>0:
                    s[i-1][j-1]+=1
                if j<w-1:
                    s[i-1][j+1]+=1
            if i<h-1:
                s[i+1][j]+=1
                if j>0:
                    s[i+1][j-1]+=1
                if j<w-1:
                    s[i+1][j+1]+=1
            if j>0:
                s[i][j-1]+=1
            if j<w-1:
                s[i][j+1]+=1

for i in range(h):
    s[i]=["#" if t<0 else t for t in s[i]]
    s[i]=[str(t) for t in s[i]]
    print("".join(s[i]))
