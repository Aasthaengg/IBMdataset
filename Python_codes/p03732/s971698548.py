N,W = map(int,input().split())
v1 = []
v2 = []
v3 = []
v4 = []
w1,v = map(int,input().split())
v1.append(v)
for i in range(N-1):
    w,v = map(int,input().split())
    if w == w1:
        v1.append(v)
    elif w == w1 + 1:
        v2.append(v)
    elif w == w1 + 2:
        v3.append(v)
    elif w == w1 + 3:
        v4.append(v)
v1.sort(reverse=True)
v2.sort(reverse=True)
v3.sort(reverse=True)
v4.sort(reverse=True)

l1 = len(v1)
l2 = len(v2)
l3 = len(v3)
l4 = len(v4)
ans = 0
for i in range(l1+1):
    for j in range(l2+1):
        for k in range(l3+1):
            for l in range(l4+1):

                if i*w1 + j*(w1+1) + k*(w1+2) + l*(w1+3) <= W:
                    temp = sum(v1[:i]) + sum(v2[:j]) + sum(v3[:k]) + sum(v4[:l])
                    ans = max(ans,temp)
print(ans)