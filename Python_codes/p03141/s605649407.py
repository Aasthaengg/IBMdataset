N = int(input())
Dishes = [list(map(int,input().split())) for _ in range(N)]
Dishes.sort(key=lambda x: x[0]+x[1])
Dishes.reverse()
score = 0
for i in range(N):
    score -= Dishes[i][1]
    if(i%2==0):
        score += Dishes[i][0] + Dishes[i][1]
print(score)