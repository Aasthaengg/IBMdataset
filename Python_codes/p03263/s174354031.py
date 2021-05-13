from sys import stdin
H,W = [int(x) for x in stdin.readline().rstrip().split()]
A = []
for i in range(H):
    a = [int(x) for x in stdin.readline().rstrip().split()]
    A.append(a)
    
ans = []

f = False
route = [0,0,0,0]
tmp = []
l = True

for h in range(H):
    for w in range(W):
        if h % 2 == 1:
            w = W-w-1
        if A[h][w] % 2 != 0:
            if not f:
                route[0],route[1] = h+1,w+1
                f = True
            else:
                route[2],route[3] = h+1,w+1
                tmp.append(route)
                route = [0,0,0,0]
                ans += tmp
                tmp = []
                f = False
        else:
            if f:
                route[2],route[3] = h+1,w+1
                tmp.append(route)
                route = [h+1,w+1,0,0]
print(len(ans))
for a,b,c,d in ans:
    print(a,b,c,d)