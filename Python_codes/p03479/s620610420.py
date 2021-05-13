x,y = map(int,input().split())

cand = [x]

while(cand[-1]*2<=y) :
    cand.append(cand[-1]*2)

print(len(cand))
