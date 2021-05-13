#!/usr/bin/env python3


def main():
    H,W,K = map(int,input().split())
    S = [input() for _ in range(H)]
    answer = [[0]*W for _ in range(H)]
    count = 0

    strobery_count = [0]*H
    for i in range(H):
        strobery_count[i] = S[i].count("#")
    flag = False
    for i in range(H):
        tmp = 1
        if strobery_count[i] == 0:
            if i >= 1:
                answer[i] = answer[i-1]
            else:
                flag = True
            continue
        
        count += 1
        for j in range(W):
            answer[i][j] = count
            if S[i][j] == "#" and tmp < strobery_count[i]:
                count += 1
                tmp += 1
    
    if flag:
        a = 0
        for i in range(H):
            if strobery_count[i] == 0:
                a = i
            else:
                a = i
                break
        
        for h in range(a):
            answer[h] = answer[a]

    for i in range(H):
        print(*answer[i])          

if __name__ == '__main__':
    main()
