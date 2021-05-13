a,b,c = map(int, input().split())
sm=a
x=a%b
sm%=b
if sm==c:
    print("YES")
    exit()

for i in range(10**5):
    sm+=a
    sm%=b
    
    if sm==c:
        print("YES")
        exit()
    elif sm==x:
        break

print("NO")
