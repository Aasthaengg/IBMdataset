import sys 
L,R = map(int, input().split())

if R-L >= 2019:
    print(0)
    sys.exit()
elif R-L == 1:
    print((R*L)%2019)
    sys.exit()

ans = 10*100
for i in range(L,R):
    for j in range(i+1,R+1):
        number = (i*j)%2019
        ans = min(ans,number)

print(ans)  