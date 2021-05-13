h,w,m = map(int,input().split())
s = set([])
H = [0]*(h+1)
W = [0]*(w+1)
for i in range(m):
    x,y = map(int,input().split())
    H[x] += 1
    W[y] += 1
    s.add((x,y))
    
p = [0]*(h+1)
q = [0]*(w+1)
for i in range(h+1):
    p[i] = [i, H[i]]
for i in range(w+1):
    q[i] = [i, W[i]]
    
p.sort(key= lambda val : val[1],reverse=True)
q.sort(key= lambda val : val[1],reverse=True)

mh = max(H)
mw = max(W)
I = H.count(mh)
J = W.count(mw)

sw = 0
for i in range(I):
    if sw == 1:
        break
    for j in range(J):
        if (p[i][0], q[j][0]) in s:
            pass
        else:
            sw = 1
            break

print(mh+mw-1+sw)
