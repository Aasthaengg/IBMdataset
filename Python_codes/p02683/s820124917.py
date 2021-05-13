scnum = list(map(int,input().split()))
score = [0]*scnum[0]
answer = 13*(10**5)
nowsum = 0
scosum = [0]*scnum[1]
gacchi = 0

for i in range(scnum[0]):
    score[i] = list(map(int,input().split()))
    
for j in range(2**scnum[0]):
    if j != 0:
        for h in range(scnum[0]):
            if (j>>h) & 1:
                nowsum += score[h][0]
                for k in range(scnum[1]):
                    scosum[k] += score[h][k+1]
        for l in range(scnum[1]):
            if scosum[l] >= scnum[2]:
                gacchi += 1
        if gacchi == scnum[1] and nowsum < answer:
            answer = nowsum
        nowsum = 0
        gacchi = 0
        scosum = [0]*scnum[1]

if answer == 13*(10**5):
    print(-1)
else:
    print(answer)