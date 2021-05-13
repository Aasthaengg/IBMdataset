N=int(input())
AB=[list(map(int,input().split())) for i in range(N)][::-1]
plus=0
for j in range(N):
    AB[j][0]+=plus
    if AB[j][0]%AB[j][1]!=0:
        a=AB[j][1]-(AB[j][0]%AB[j][1])
        AB[j][0]+=a
        plus+=a
print(plus)