N= int(input())
E = [input().split()[2:] for _ in [0]*N]
Q = [0]
L = [0] + [-1]*N

    


while Q:
    top = Q.pop(0)
    for i in E[top]:
        i = int(i) - 1
        if L[i] < 0 :L[i] = L[top] +1 ; Q+= [i]

for i in range(N):print(i + 1 ,int(L[i]))

