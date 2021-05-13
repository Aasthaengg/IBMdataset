N,K = list(map(int,input().split()))
X = list(map(int,input().split()))
l = 0
r = K-1
outs = []
while r<=N-1:
    A = X[l]
    B = X[r]
    if A<0 and B<0:
        out = -1*A
    if A<0 and B>=0:
        out = min(-1*A*2+B,-1*A+2*B)
    if A>=0 and B>=0:
        out = B
    outs.append(out)
    l+=1
    r+=1
print(min(outs))
