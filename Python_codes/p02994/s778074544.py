a,b=map(int, input().split())
L = []

for i in range(1,a+1):
    L.append(b+i-1)

if L[0] >= 0:
    L[0] = 0
    print(sum(L))
if L[0] < 0 and L[a-1] > 0:
    print(sum(L))
if L[0] < 0 and L[a-1] <= 0:
    L[a-1] = 0
    print(sum(L))