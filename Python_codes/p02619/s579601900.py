import random

def down_score(d, c, last_d, score):
    sum = 0
    for i in range(26):
        sum = sum + c[i]*(d-last_d[i])
        
    return int(score - sum)


def main():
    D = int(input())

    c = list(map(int, input().split()))

    s = [list(map(int, input().split())) for i in range(D)]

    sche = []
    for i in range(D):
        x = int(input())
        sche.append(x)
    
    last_d = [0 for i in range(26)]
    score = 0
    
    for i in range(D):
        score += s[i][sche[i]-1]
        last_d[sche[i]-1] = i+1
        score = down_score(i+1, c, last_d, score)
        print(score)
        
if __name__ == "__main__":
    main()
