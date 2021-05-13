a,b,c = map(int, input().split())
sm=0
for i in range(10**5):
    sm+=a
    sm%=b
    
    if sm==c:
        print("YES")
        exit()

print("NO")
