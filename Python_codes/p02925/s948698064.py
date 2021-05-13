n=int(input())
match=[]
for i in range(n):
    a=list(map(int, input().split()))
    match.append(a)

select=[list(range(n))]

day=0
mat=0
for _ in range(int(n*(n-1)/2)):
    nex=[]
    for x in select[day]:
        if len(match[x]) != 0 and not x in nex and not match[x][0]-1 in nex and match[match[x][0]-1][0] == (x+1):
            nex.append(x)
            nex.append(match[x][0]-1)
            match[match[x][0]-1].pop(0)
            match[x].pop(0)
            mat+=1

    if len(nex) == 0 and mat==int(n*(n-1)/2):
        break
    
    if len(nex) == 0:
        print(-1)
        exit()

    select.append(nex)
    day+=1

print(day)