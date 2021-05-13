import sys
readline = sys.stdin.buffer.readline
N,W = map(int,readline().split())
w,v = map(int,readline().split())
tmp = w
lst1 = [1,0,0,0]
v0 = [v]
v1 = []
v2 = []
v3 = []
for i in range(N-1):
    w,v = map(int,readline().split())
    if w == tmp:
        lst1[0] += 1
        v0.append(v)
    elif w == tmp+1:
        lst1[1] += 1
        v1.append(v)
    elif w == tmp+2:
        lst1[2] += 1
        v2.append(v)
    else:
        lst1[3] += 1
        v3.append(v)
v0.sort(reverse=True)
for i in range(1,lst1[0]):
    v0[i] += v0[i-1]
v1.sort(reverse=True)
for i in range(1,lst1[1]):
    v1[i] += v1[i-1]
v2.sort(reverse=True)
for i in range(1,lst1[2]):
    v2[i] += v2[i-1]
v3.sort(reverse=True)
for i in range(1,lst1[3]):
    v3[i] += v3[i-1]

ans = 0
for i in range(lst1[0]+1):
    for j in range(lst1[1]+1):
        for k in range(lst1[2]+1):
            for l in range(lst1[3]+1):
                res = i*tmp+j*(tmp+1)+k*(tmp+2)+l*(tmp+3)
                if W >= res:
                    res2 = 0
                    if i != 0:
                        res2 += v0[i-1]
                    if j != 0:
                        res2 += v1[j-1]
                    if k != 0:
                        res2 += v2[k-1]
                    if l != 0:
                        res2 += v3[l-1]


                    ans = max(ans,res2)

print(ans)