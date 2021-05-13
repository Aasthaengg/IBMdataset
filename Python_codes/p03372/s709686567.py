n,c = map(int,input().split())
sushi = [[0,0]]
for i in range(n):
    x,v = map(int,input().split())
    sushi.append([x,v])

###はじめ反時計回りに回る場合
score = [0 for i in range(n+1)] #時計回りでk番目までの寿司が食べられる時、最大摂取カロリーを記録する
start = 0
noteat = 0
for i in range(1,n+1):
    temp = 0
    if score[i-1] - (sushi[i][0] - start) + sushi[i][1] + noteat > score[i-1]: #寿司を食べた場合
        temp = score[i-1] - (sushi[i][0] - start) + sushi[i][1] + noteat
        noteat = 0
        start = sushi[i][0]
    else:
        noteat += sushi[i][1]
        temp = score[i-1]
    score[i] = temp



ans = score[n]
leftscore = 0
dist = 0
for i in range(1,n): #i個は反時計回りに食べてから時計回りに戻る
    leftscore += sushi[-i][1]
    if i == 1:
        dist += c - sushi[-i][0]
    else:
        dist += sushi[-i+1][0] - sushi[-i][0]
    if leftscore - 2*dist + score[n-i] > ans:
        ans = leftscore - 2*dist + score[n-i]


#######

#######はじめ時計回りに回る場合
reverse = [0 for i in range(n+1)]
start = c
noteat = 0
for i in range(1,n+1):
    temp = 0
    if sushi[-i][1] - (start - sushi[-i][0]) + reverse[i-1] + noteat > reverse[i-1]: #寿司を食べた場合
        temp = sushi[-i][1] - (start - sushi[-i][0]) + reverse[i-1] + noteat
        noteat = 0
        start = sushi[-i][0]
    else:
        noteat += sushi[-i][1]
        temp = reverse[i-1]
    reverse[i] = temp



ans2 = reverse[n]
rightscore = 0
dist = 0
for i in range(1,n): #i個時計回りに食べてから戻る
    rightscore += sushi[i][1]
    dist += sushi[i][0] - sushi[i-1][0]
    if rightscore - 2*dist + reverse[n-i] > ans2:
        ans2 = rightscore - 2*dist + reverse[n-i]

print(max(ans,ans2))