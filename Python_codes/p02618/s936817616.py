import copy as cp
#INPUT
D = int(input())
c = [int(i) for i in input().split()]
s = []
for i in range(D):
    new = [int(i) for i in input().split()]
    s.append(new)

#Utilitiy
def score(ans):
    if len(ans) != D:
        print("wrong length")
        return 0
    else:
        p = 0
        last = [-1]*26
        for i in range(D):
            contest = ans[i]-1
            p += s[i][contest]
            last[contest] = i
            for j in range(26):
                p -= c[j]*(i-last[j])
        return p

def greedy(ahead=0):
    ans = []
    p = 0
    last = [-1]*26
    for i in range(D):
        decay = 0
        for j in range(26):
            decay -= c[j]*(i-last[j])
            
        max_j = -1
        max_plus_mod = decay
        max_plus = decay
        for j in range(26):
            plus = s[i][j] + c[j]*(i-last[j])
            modify = c[j]*(ahead*(i-last[j])+ahead*(ahead+1)//2)
            if (plus+modify) > max_plus_mod:
                max_plus = plus
                max_plus_mod = plus+modify
                max_j = j
        ans.append(max_j+1)
        last[max_j]=i
        p += max_plus + decay
    return ans, p
        
#MAIN
max_points = -10000000
for k in range(20):
    ans_temp, points = greedy(ahead = k)
    #print(k, points, ans_temp)
    if points > max_points:
        max_points = points
        ans = cp.copy(ans_temp)

for i in range(D):
    print(ans[i])