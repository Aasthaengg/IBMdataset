from collections import deque

H,W = map(int,input().split())

S = []

for i in range(H):

    s = input()

    S.append(s)

lis = [ [True] * W for i in range(H) ]

ans = 0

for h in range(H):

    for w in range(W):

        if not lis[h][w]:
            continue
        
        q = deque([[h,w]])
        lis[h][w] = False

        if S[h][w] == "#":
            bnum = 1
            wnum = 0
        else:
            bnum = 0
            wnum = 1

        while len(q) > 0:

            now = q.popleft()
            nh = now[0]
            nw = now[1]

            if S[nh][nw] == "#":

                if nh > 0 and S[nh-1][nw] == "." and lis[nh-1][nw]:

                    wnum += 1
                    lis[nh-1][nw] = False
                    q.append([nh-1,nw])

                if nh < H-1 and S[nh+1][nw] == "." and lis[nh+1][nw]:

                    wnum += 1
                    lis[nh+1][nw] = False
                    q.append([nh+1,nw])

                if nw > 0 and S[nh][nw-1] == "." and lis[nh][nw-1]:

                    wnum += 1
                    lis[nh][nw-1] = False
                    q.append([nh,nw-1])

                if nw < W-1 and S[nh][nw+1] == "." and lis[nh][nw+1]:

                    wnum += 1
                    lis[nh][nw+1] = False
                    q.append([nh,nw+1])

            if S[nh][nw] == ".":

                if nh > 0 and S[nh-1][nw] == "#" and lis[nh-1][nw]:

                    bnum += 1
                    lis[nh-1][nw] = False
                    q.append([nh-1,nw])

                if nh < H-1 and S[nh+1][nw] == "#" and lis[nh+1][nw]:

                    bnum += 1
                    lis[nh+1][nw] = False
                    q.append([nh+1,nw])

                if nw > 0 and S[nh][nw-1] == "#" and lis[nh][nw-1]:

                    bnum += 1
                    lis[nh][nw-1] = False
                    q.append([nh,nw-1])

                if nw < W-1 and S[nh][nw+1] == "#" and lis[nh][nw+1]:

                    bnum += 1
                    lis[nh][nw+1] = False
                    q.append([nh,nw+1])
                    
        ans += wnum * bnum


print (ans)

                

