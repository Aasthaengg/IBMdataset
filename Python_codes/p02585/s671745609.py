#D - Moving_piece
N,K = map(int,input().split())
P =[]
C =[]
P = list(map(int,input().split()))
C = list(map(int,input().split()))

score_output = -1000000000
i = 0
for i in range(N):
    ichi = i
    score = 0
    step  = 0
    loop  = 0
    score_max = -1000000000
    while True:
        step  += 1
        score += C[ichi]
        ichi   = (P[ichi] -1)
        if i ==  (P[ichi] -1):
            score += C[ichi]
            break
        
    path = 0
    cnt  = 0
    
    while True:
        cnt  += 1
        path += C[ichi]
        
        if cnt > K:
            break
        
        loop = int((K - cnt) / (step+ 1))
        if score > 0:
            score_max = path + loop * score
        else:
            score_max = path
        if score_max > score_output:
            score_output = score_max

        ichi   = P[ichi]-1
        if i == (P[ichi] -1):
            break
# 出力
print(score_output)
