H,W = map(int,input().split())
l=[]
for i in range(H):
    l.append(list(input()))
for i in range(H):
    for count in range(2):
        for j in range(W):
            if j==W-1:
                print(l[i][j])
            else:
                print(l[i][j],end='')
