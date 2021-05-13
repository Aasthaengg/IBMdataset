n=int(input())

AB=[list(map(int,input().split())) for i in range(n)]

AB.sort(key=lambda x:x[0]+x[1],reverse=True)

if len(AB)%2==1:
    AB.append([0,0])

s=0
for i in range(0,len(AB),2):
    s+=AB[i][0]-AB[i+1][1]

print(s)