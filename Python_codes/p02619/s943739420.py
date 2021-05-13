D = int(input())
C = list(map(int,input().split()))
S = [list(map(int,input().split())) for i in range(D)]
T = [int(input()) for i in range(D)]

last = [0] * 26
score = 0
for i,(s,a) in enumerate(zip(S,T)):
    score += s[a-1]
    last[a-1] = i+1
    for j,c in enumerate(C):
        score -= c * (i+1 - last[j])
    print(score)