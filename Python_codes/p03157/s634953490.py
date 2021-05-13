h,w = map(int, input().split())
s = [input() for i in range(h)]

visited = [[0]*w for i in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        black = 0
        white = 0
        stack = [[i,j]]
        while stack:
            a,b = stack.pop()
            if visited[a][b]!=1:
                visited[a][b]+=1
                if s[a][b]=='#':
                    black+=1
                else:
                    white+=1
                for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                    c = a+y
                    d = b+x
                    if 0<=c<h and 0<=d<w:
                        if s[a][b]!=s[c][d]:
                            stack.append([c,d])
        ans += black*white
print(ans)


