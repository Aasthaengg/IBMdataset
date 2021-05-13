from collections import deque
H,W=map(int,input().split())
S=[input() for i in range(H)]
checked=[[0 for i in range(W)] for m in range(H)]

count=0
count2=0
visited=set()
for h1 in range(H):
    for w1 in range(W):
        if S[h1][w1]=="#" and checked[h1][w1]==0:
            checked[h1][w1]=1
            stack=deque([[h1,w1,"#"]])
            kuro=1
            siro=0
            count2+=1
            visited.add(h1*400+w1)
            while stack:
                h,w,iro=stack.popleft()
                for y,x in [[-1,0],[1,0],[0,1],[0,-1]]:
                    Y,X=y+h,x+w
                    visitednum=Y*400+X
                    if 0<=Y<H and 0<=X<W and not visitednum in visited:
                        if iro=="#" and S[Y][X]==".":
                            siro+=1
                            visited.add(visitednum)
                            stack.append([Y,X,"."])
                        elif iro=="." and S[Y][X]=="#" and not visitednum in visited:
                            kuro+=1
                            checked[Y][X]=1
                            visited.add(visitednum)
                            stack.append([Y,X,"#"])
            count+=kuro*siro
print(count)
