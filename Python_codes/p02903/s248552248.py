def main(H,W,A,B):
    ans = [[] for _ in range(H)]
    #print(ans)
    cntB = 0
    for i in range(H):
        cntB += 1
        cntA = 1
        for j in range(W):
            if cntB <= B:
                if cntA <= A:
                    ans[i].append(0)
                    cntA += 1
                else:
                    ans[i].append(1)
            else:
                if cntA <= A:
                    ans[i].append(1)
                    cntA += 1
                else:
                    ans[i].append(0)
    return ans

H,W,A,B = map(int,input().split())
ans = main(H,W,A,B)
for i in range(H):
    tmp = ans[i]
    tmp = map(str,tmp)
    print(''.join(tmp))
