a,b,c = map(int,input().split())
ans = 0
for i in range(1,b+1):
    if (a*i)%b == c:
        ans = 1
        break
print(["NO","YES"][ans])