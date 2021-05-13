
p1 = [0,0]
p2 = [100,0]
R = [[0.5,-1.7320508/2],[1.7320508/2,0.5]]

def dot(A,b):
    vs = [0,0]
    for i in range(2):
        for j in range(2):
            vs[i] += A[i][j]*b[j]
    return vs

def diff(p1,p2):
    return [(p1[0]-p2[0])/3.0,(p1[1]-p2[1])/3.0]

def sumV(p1,p2):
    return [p1[0]+p2[0],p1[1]+p2[1]]

def new_koch(p1,p2):
    p = diff(p2,p1)
    p_new1 = sumV(p1,p)
    p_new2 = sumV(p_new1,dot(R,p))
    p_new3 = sumV(p1,sumV(p,p))
    return [p1,p_new1,p_new2,p_new3]

n = int(input())
ps = [p1,p2]
for i in range(n):    
    X = len(ps)
    ps_new = []
    for i in range(X-1):
        ps_new.extend(new_koch(ps[i],ps[i+1]))
    ps_new += [ps[-1]]
    ps = [p for p in ps_new]

for p in ps:
    print(*p)


