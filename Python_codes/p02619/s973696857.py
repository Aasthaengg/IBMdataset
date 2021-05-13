
D = int(input())
# with open("sample1.in") as f:

last = [0 for i in range(26)]
s = [[0 for j in range(26)] for i in range(D)]
c = list(map(int, input().split(" ")))
result = []
# opened = []  #開催したやつを保存
for i in range(D):
    a = list(map(int, input().split(" ")))
    for j, k in enumerate(a):
        #print(i, j, k)
        s[i][j] = int(k)
        # スコア計算
        
for i in range(D):  
    result.append(int(input()))
score_max=0
for i in range(D):
    #score_max = 0
    score_index = 0
    tmp=result[i]-1
    score=s[i][tmp]+(i + 1 - last[tmp]) * c[tmp]
    #print("score",s[i][tmp])
    for j in range(26):
        score -= (i + 1 - last[j]) * c[j]
    #print("score-",score)
    score_max+=score
    print(score_max)
    last[tmp] = i+1
    
    # print(s.index(max(s[i])))
    # print(result[i]+1)
