from collections import defaultdict

def cumsum(ls):
    for i in range(1,len(ls)):
        ls[i] += ls[i-1]
    ls.insert(0,0)
    return ls

def main():
    n,w = map(int,input().split())
    dc = defaultdict(list)
    W1,V1 = map(int,input().split())
    dc[W1].append(V1)
    for _ in range(1,n):
        wk,vk = map(int,input().split())
        dc[wk].append(vk)

    #　下準備
    dc = sorted(dc.items(),key=lambda x:x[0],reverse=True)
    for i in range(len(dc)):
        dc[i] = list(dc[i])
        dc[i][1] = cumsum(sorted(list(dc[i][1]),reverse=True))
    
    for i in range(4-len(dc)):
        dc.append([0,[0]])
    can = [0,0] # [w,v]
    ans = 0
    for i in range(len(dc[0][1])):
        for j in range(len(dc[1][1])):
            for k in range(len(dc[2][1])):
                for l in range(len(dc[3][1])):
                    can[0] = dc[0][0]*i + dc[1][0]*j + dc[2][0]*k + dc[3][0]*l
                    can[1] = dc[0][1][i] + dc[1][1][j] + dc[2][1][k]+ dc[3][1][l]
                    if can[0]<=w:
                        ans = max(ans,can[1])
                    can = [0,0]
    print(ans)
if __name__ == "__main__":
    main()