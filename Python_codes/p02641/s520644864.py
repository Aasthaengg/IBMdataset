import bisect
X,N = map(int,input().split())

p = list(map(int,input().split()))
p = sorted(p,reverse = False)
p_x = []
if p == []:
    print(X)
else:
    for i in range(200):
        if not(i in p):
            p_x.append(i)
    idx_x = bisect.bisect_left(p_x,X)
    if abs(X-p_x[idx_x-1]) < abs(X-p_x[idx_x]):
           print(p_x[idx_x-1])
    elif abs(X-p_x[idx_x-1]) > abs(X-p_x[idx_x]):
           print(p_x[idx_x])
    else:
        print(min(p_x[idx_x],p_x[idx_x-1]))