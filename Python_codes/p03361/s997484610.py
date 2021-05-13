def check():
    H, W = map(int, input().split())
    S = [0]*(H+2)
    S[0] = '.'*(W+2)
    S[H+1] = '.'*(W+2)
    for h in range(1,H+1):
        S[h] = '.' + input() + '.'
    
    dh = [0,1,0,-1]
    dw = [1,0,-1,0]
    
    for h in range(1,H+1):
        for w in range(1,W+1):
            if S[h][w]=='.':
                continue
            for i in range(4):
                h0 = h+dh[i]
                w0 = w+dw[i]
                if S[h0][w0]=='#':
                    break
            else:
                return 'No'
    return 'Yes'
    
print(check())