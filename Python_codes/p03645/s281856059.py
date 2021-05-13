n,m=map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

l1=[0]*n
ln=[0]*n
for i in range(m):
    if ab[i][0]==1:
        l1[ab[i][1]-1]+=1
    if ab[i][1]==n:
        ln[ab[i][0]-1]+=1
    #print(l1,ln)
for i in range(n):
    if l1[i]!=0 and ln[i]!=0:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")