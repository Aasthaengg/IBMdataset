import random
import time

def down_score(d, c, last_d, score):
    sum = 0
    for i in range(26):
        sum = sum + c[i]*(d-last_d[i])
        
    return int(score - sum)


def main():
    D = int(input())

    c = list(map(int, input().split()))

    s = [list(map(int, input().split())) for i in range(D)]

    start = time.time()
    
    last_d = [0 for i in range(26)]
    
    ans = []
    
    score1 = 0
    
    for i in range(D):
        max = 0
        idx = 0
        for j in range(26):
            if max < (s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2) and c[j] != 0:
                max = s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2
                idx = j
            elif max == (s[i][j] + c[j] * (i-last_d[j])*(i-last_d[j]+1)/2) and c[j] * (i-last_d[j])*(i-last_d[j]+1)/2 > c[idx]* (i-last_d[idx])*(i-last_d[idx]+1)/2 and c[j] != 0:
                idx = j
            
        last_d[idx] = i+1
        score1 += s[i][idx]
        score1 = down_score(i+1,c,last_d,score1)
        
        ans.append(idx)

    while time.time() - start < 1.9:
        d1 = random.randint(0,D-19)
        d2 = random.randint(d1+1,d1+18)
        if d1 == d2:
            continue
        tmp_d1 = ans[d1]
        tmp_d2 = ans[d2]
        ans[d1] = tmp_d2
        ans[d2] = tmp_d1
        last_d = [0 for i in range(26)]
        score2 = 0    
        for i in range(D):
            score2 += s[i][ans[i]]
            last_d[ans[i]] = i+1
            score2 = down_score(i+1, c, last_d, score2)
        
        if score1 > score2:
            ans[d1] = tmp_d1
            ans[d2] = tmp_d2
        else:
            score1 = score2
    
    for i in range(D):
        print(ans[i]+1)  

if __name__ == "__main__":
    main()

"""
101283559

"""