N = int(input())
Nlist = [[] for _ in range(N)]
for i in range(N):
    C, P = input().split()
    P = int(P)
    Nlist[i].append(i+1)
    Nlist[i].append(C)
    Nlist[i].append(P)

Nlist.sort(key=lambda x: x[1])
Nlist.sort(key=lambda x: x[2],reverse=True)
Nlist.sort(key=lambda x: x[1])
for i in range(N):
    print(Nlist[i][0])
