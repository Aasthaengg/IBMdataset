s = list(str(input()))
K = int(input())
N = len(s)

L = list("abcdefghijklmnopqrstuvwxyz")

def dictmin(p,q):
    ret = -1
    for i in range(len(p)):
        if i >= len(q):
            ret = q
            break
        elif L.index(p[i]) < L.index(q[i]):
            ret = p
            break
        elif L.index(p[i]) > L.index(q[i]):
            ret = q
            break
    if ret == -1:
        ret = p
    return ret

def renew(X,p):
    for i in range(K):
        if X[i] == p:
            break
        elif dictmin(X[i],p) == p:
            for j in range(K-1,i,-1):
                X[j] = X[j-1]
            X[i] = p
            break
    return X
        
count = 0
can = [["z"]*6 for i in range(K)]

for x in L:
    for i in range(N):
        if s[i] == x:
            count += N-i
            for j in range(i,min(i+5,N)):
                #print(s[i:(j+1)])
                can = renew(can,s[i:(j+1)])
                #print(x,i,count,can)
    if can[K-1] != ["z"]*6:
        break

print("".join(can[K-1]))

