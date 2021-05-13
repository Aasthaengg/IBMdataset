C = {i:0 for i in range(9)}
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    a = A[i]
    if a<400:
        C[0] += 1
    elif a<800:
        C[1] += 1
    elif a<1200:
        C[2] += 1
    elif a<1600:
        C[3] += 1
    elif a<2000:
        C[4] += 1
    elif a<2400:
        C[5] += 1
    elif a<2800:
        C[6] += 1
    elif a<3200:
        C[7] += 1
    else:
        C[8] += 1
cmin = 0
for i in range(8):
    if C[i]>0:
        cmin += 1
if cmin==0:
    cmin = 1
    cmax = C[8]
else:
    cmax = cmin+C[8]
print(cmin,cmax)