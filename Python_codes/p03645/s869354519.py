N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

lst1 = []
lstN = []

for i in range(M):
    if AB[i][0] == 1:
        lst1.append(AB[i][1])
    if AB[i][1] == N:
        lstN.append(AB[i][0])

if list(set(lst1) & set(lstN)) == []:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")