A,B=map(int,input().split())
cookie=[A,B,A+B]
for i in range(3):
    cookie[i]%=3

if 0 in cookie:
    print("Possible")
else:
    print("Impossible")