n = int(input())
V = list(map(int,input().split()))
Ce = {}
Co = {}
for i in range(n):
    v = V[i]
    if i%2==0:
        if v not in Ce:
            Ce[v]=0
        Ce[v] += 1
    else:
        if v not in Co:
            Co[v]=0
        Co[v] += 1
Ce = sorted(list(Ce.items()),key=lambda x:x[1],reverse=True)
Co = sorted(list(Co.items()),key=lambda x:x[1],reverse=True)
if Ce[0][0]!=Co[0][0]:
    cnt = 0
    for i in range(1,len(Ce)):
        cnt += Ce[i][1]
    for i in range(1,len(Co)):
        cnt += Co[i][1]
    print(cnt)
else:
    cnt1 = 0
    for i in range(1,len(Ce)):
        cnt1 += Ce[i][1]
    if Ce[0][1]>n//2:
        cnt1 += Ce[0][1]-n//2
    cnt1 += Co[0][1]
    for i in range(2,len(Co)):
        cnt1 += Co[i][1]
    cnt2 = 0
    for i in range(1,len(Co)):
        cnt2 += Co[i][1]
    if Co[0][1]>n//2:
        cnt2 += Co[0][1]-n//2
    cnt2 += Ce[0][1]
    for i in range(2,len(Ce)):
        cnt2 += Ce[i][1]
    print(min(cnt1,cnt2))