D = int(input())
c = list(map(int,input().split()))
s = [list(map(int, input().split())) for l in range(D)]
t = [int(input()) for i in range(D)]
score = 0
last = [0]*26

def score_down(d):
    ans = 0
    for i in range(26):
        ans += c[i]*(d - last[i])
    return ans

for d in range(len(t)):
    i = t[d] - 1
    last[i] = d+1
    score += s[d][i]
    score -= score_down(d+1)
    print(score)