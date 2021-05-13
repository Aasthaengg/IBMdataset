n=int(input())
D=[list(map(int,input().split())) for _ in range(n)]

cnt=0
for a,b in D:
    if a==b:cnt +=1
    else:cnt=0

    if cnt==3:print("Yes");exit()
print("No")