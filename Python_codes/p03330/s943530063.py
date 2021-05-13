N,C = map(int,input().split())
Color = []
for _ in range(C):
    Color.append(list(map(int,input().split()))) 
Data = []
for _ in range(N):
    Data.append(list(map(int,input().split()))) 

Data2 = [{},{},{}]

for h in range(N):
    for w in range(N):
        c = Data[h][w]
        m = (h + w) % 3
        if not c in Data2[m]:
            Data2[m][c] = 0 
        Data2[m][c]+=1

ans = 10**20
for c1 in range(C):
    for c2 in range(C):
        if c1 == c2:
            continue
        for c3 in range(C):
            if c1 == c3 or c2 == c3:
                continue

            tmp = 0
            for k,v in Data2[0].items():
                tmp += (Color[k-1][c1-1]*v)
            for k,v in Data2[1].items():
                tmp += (Color[k-1][c2-1]*v)
            for k,v in Data2[2].items():
                tmp += (Color[k-1][c3-1]*v)
            ans = min(ans,tmp)

print(ans)
