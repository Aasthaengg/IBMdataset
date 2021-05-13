a,b= map(int, input().split())
dif=b-a
sm=0
for i in range(dif):
        sm+=i
print(sm-a)