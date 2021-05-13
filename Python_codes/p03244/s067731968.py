n = int(input())
V = list(map(int,input().split()))
Ce = {}
Co = {}
for i in range(n):
    v = V[i]
    if i%2==0:
        if v not in Ce:
            Ce[v] = 0
        Ce[v] += 1
    else:
        if v not in Co:
            Co[v] = 0
        Co[v] += 1
Ce = sorted(list(Ce.items()),key=lambda x:x[1],reverse=True)
Co = sorted(list(Co.items()),key=lambda x:x[1],reverse=True)
if len(Ce)==1 and len(Co)==1 and Ce[0][0]==Co[0][0]:
    m = n//2
else:
    if Ce[0][0]!=Co[0][0]:
        m = n-Ce[0][1]-Co[0][1]
    else:
        m1 = n-Ce[1][1]-Co[0][1]
        m2 = n-Ce[0][1]-Co[1][1]
        m = min(m1,m2)
print(m)