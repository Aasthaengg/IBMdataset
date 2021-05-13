X,Y=map(int,input().split())
ans = 0
num = X
while num <= Y:
    num *= 2
    ans += 1
print(ans)