N = int(input())
score = []

for i in range(N):
    a, b = map(int, input().split())
    score.append([a,b])

score.sort(key = lambda x:x[0])

ans = score[0][0]

for i in range(1,N):
    ans += score[i][0] - score[i-1][0]
    
if score[-1][1] != 0:
    ans += score[-1][1]

print(ans)