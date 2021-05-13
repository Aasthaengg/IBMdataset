N= int(input())
E = [input().split()[2:] for _ in [0]*N]
Q = [0]
L = [0] + [-1]*N
def func(ide):
    global Q
    for i in E[ide]:
        i = int(i) - 1
        if L[i] < 0 :L[i] = L[ide] +1 ;Q += [i]
    

while Q:top = Q.pop(0);func(top)

for i in range(N):print(i + 1 ,int(L[i]))

