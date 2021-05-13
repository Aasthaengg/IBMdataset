# AGC 012 A - AtCoder Group Contest
N = int(input())
an = list(map(int,input().split()))

lists = [[] for _ in range(N)]
an.sort(reverse=True)

for k in range(N):
    lists[k].append(an[2*k])
    lists[k].append(an[2*k+1])
                    
for i in range(N):
    lists[i].append(an[2*N-1+i])

sasa = 0
for j in range(N):
    sasa += lists[j][1]
print(sasa)