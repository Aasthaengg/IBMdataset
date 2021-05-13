N,C = map(int,input().split())
src = [tuple(map(int,input().split())) for i in range(N)]

cumsumr = [0]
cummaxr = [0]
cummaxr2 = [0]
px = 0
for x,v in src:
    cumsumr.append(cumsumr[-1] + v-(x-px))
    cummaxr.append(max(cummaxr[-1], cumsumr[-1]))
    cummaxr2.append(max(cummaxr2[-1], cumsumr[-1]-x))
    px = x

cumsuml = [0]
cummaxl = [0]
cummaxl2 = [0]
px = C
for x,v in src[::-1]:
    cumsuml.append(cumsuml[-1] + v-(px-x))
    cummaxl.append(max(cummaxl[-1], cumsuml[-1]))
    cummaxl2.append(max(cummaxl2[-1], cumsuml[-1]-(C-x)))
    px = x

ans = max(cummaxr[-1], cummaxl[-1])
for i in range(N):
    ans = max(ans, cummaxr2[i] + cummaxl[N-i])
    ans = max(ans, cummaxl2[i] + cummaxr[N-i])
print(ans)