n=int(input())
l=[[0,0,0]]
for _ in range(n):
    l.append(list(map(int,input().split())))

for i in range(1,n+1):
    k=abs(l[i][1]-l[i-1][1])+abs(l[i][2]-l[i-1][2])
    t=l[i][0]-l[i-1][0]
    if k>t or k%2!=t%2:
        print("No")
        exit()
print("Yes")