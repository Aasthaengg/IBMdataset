global t
t = 0

class Node:
    def __init__(self, num, deg, neib):
        self.num = num
        self.deg = deg
        self.neib = neib

def dfs(G, d, f, now): #now:1,2,...
    #print("now:",now)
    global t
    t += 1
    #print("t:",t)
    if d[now-1] != 0:
        t -= 1
        #print("has searched or hit roop")
    else:
        d[now-1] = t
        #print("d:",d)
        #print("f:",f)
        for i in G[now-1].neib:
            #print("i:",i)
            if i != -1:
                #print("next node")
                dfs(G, d, f, i)
            #else: print("end of branch")
        t += 1
        f[now-1] = t

        #print("f:",f)


dnum = int(input()) #頂点数
N = []
for i in range(dnum):
    data = input().split()
    
    u = int(data[0])
    k = int(data[1])
    if k > 0:
        v = list(map(int, data[2:]))
    else:
        v = [-1]

    node = Node(u,k,v)
    N.append(node)

d = [0]*dnum #find time
f = [0]*dnum #finish time

while 0 in d:
    s = d.index(0)
    dfs(N, d, f, s+1)
    #print("looks like finish")

for i in range(dnum):
    print(i+1, d[i], f[i])

