n,m = map(int,input().split())
ag = []
for i in range(n):
    ag.append(list(input()))
bg = []
for i in range(m):
    bg.append(list(input()))
for i in range(n-m+1):
    for j in range(n-m+1):
        u = []
        for k in range(m):
            u.append(ag[j+k][i:i+m])
        if u == bg:
            print("Yes")
            exit()
print("No")



