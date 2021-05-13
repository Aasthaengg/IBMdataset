A,B=map(int,input().split())
G=[['.']*100 for i in range(100)]

for i in range(50):
    for j in range(100):
        G[i][j]='#'




white,black=1,1

for i in range(0,50,2):
    for j in range(0,100,2):
        if white==A:
            break
        G[i][j]='.'
        white+=1

for i in range(51,100,2):
    for j in range(0,100,2):
        if black==B:
            break
        G[i][j]='#'
        black+=1

print(100,100)
for i in range(100):
    print(*G[i],sep='')