H,W = map(int,input().split())
S = [['x'] * (W+2)]
for i in range(H) :
    s1 = ['x']
    s1 += list(input())
    s1.append('x')
    S.append(s1)

S.append(['x'] * (W+2))
around = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
for i in range(H+1) :
    for j in range(W+1) :
        if S[i][j] == '.' :
#            print('S[{}][{}]'.format(i,j))
            count = 0
            for k in range(8) :
                if S[i+around[k][0]][j+around[k][1]] == '#' :
#                    print('         around[{}] = {}'.format(k,around[k]))
#                    print('             S[{}][{}] = #'.format(i+around[k][0],j+around[k][1]))
                    count += 1
            S[i][j] = count

ans = ['']* H
for i in range(1,H+1) :
    for j in range(1,W+1) :
        ans[i-1] += str(S[i][j])
    print(ans[i-1])
