H,W=map(int,input().split())


S = [input() for i in range(H)]

ans = S

for i,row in enumerate(S):
    for j,mas in enumerate(row):
        if mas == '#':
            pass
        else:
            count = 0
            for i2 in [-1,0,1]:
                for j2 in [-1,0,1]:
                    if (i+i2<0) | (j+j2<0) | (i+i2>=H) |(j+j2>=W):
                        pass
                    else:
                        if S[i+i2][j+j2]=='#':
                            count +=1
            ans[i] = ans[i][:j] + str(count) +ans[i][j+1:]
for i in ans:
    print(i)