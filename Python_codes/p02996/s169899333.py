n = int(input())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append([b,a])
lst.sort()

time = 0
for i in range(n):
    simekiri, sigoto = lst[i][0],lst[i][1]
    time += sigoto
    if time <= simekiri:
        continue
    else:
        print('No')
        exit()
print('Yes')