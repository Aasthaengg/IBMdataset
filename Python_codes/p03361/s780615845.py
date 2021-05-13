import sys
h,w=map(int,input().split())
s=[input() for i in range(h)]
ss=[[0 for _ in range(w+2)] for _ in range(h+2)]
for j in range(w):
    for i in range(h):
        ss[i+1][j+1]=s[i][j]
for j in range(1,w+1):
    for i in range(1,h+1):
        c=True
        if ss[i][j]=='.':
            continue
        if not(ss[i-1][j]=='#' or ss[i][j-1]=='#' or ss[i][j+1]=='#' or ss[i+1][j]=='#'):
            print('No')
            sys.exit()
print('Yes')