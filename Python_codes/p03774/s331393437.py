def minDistPoint(Student,List):
    ans_dist = 500000000
    res = 0
    for k,pos in List.items():
        dist = abs(Student[0]-pos[0])+abs(Student[1]-pos[1])
        if dist<ans_dist:
            ans_dist = dist
            res=k
    return res+1

N,M=map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
CD = {i:list(map(int,input().split())) for i in range(M)}

cp = [0]*N

for i in range(len(AB)):
    cp[i] = minDistPoint(AB[i],CD)
    
for i in cp:
    print(i)