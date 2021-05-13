N = int(input())
saying =[]
people =[]
result = 0

for i in range(N):
    A=int(input())
    people.append(0)
    saying.append([])
    for j in range(A):
        x, y = map(int,input().split())
        saying[i].append(x)
        saying[i].append(y)

for i in range(2**N):

    for j in range(N):
        if(i & 1<<j):
            people[j]=1
        else:
            people[j]=0
    honest = 0
    for j in range(N):
        if people[j]==1:
            for k in range(0, len(saying[j]),2):
                if people[saying[j][k]-1] != saying[j][k+1]:
                    break
            else:
                honest += 1
                continue
            break
    else:
        if honest>result:
            result = honest

print(result)