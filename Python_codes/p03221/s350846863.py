n,m = map(int,input().split())
p = [0]*m
V = [[] for i in range(n+1)]
for i in range(m):
    p[i] = list(map(int,input().split())) + [i]
    V[p[i][0]].append(p[i][1:])
W = []
for i in range(n+1):
    if V[i] == []:
        pass
    else:
        V[i].sort(key= lambda val : val[0])
        for j in range(len(V[i])):
            K = ["0"]*(6 - len(str(i))) + list(str(i)) + ["0"]*(6 - len(str(j+1))) + list(str(j+1))
            W.append(["".join(K),V[i][j][1]])
W.sort(key= lambda val : val[1])
for ans in W:
    print(ans[0])
        
    

