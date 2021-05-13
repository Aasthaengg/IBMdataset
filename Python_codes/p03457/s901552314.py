n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]
T=X=Y=0
ans = "Yes"
for t,x,y in txy:
    if abs(T-t) < abs(X-x)+abs(Y-y):
        ans = "No"
        break
    a = abs(T-t) - (abs(X-x)+abs(Y-y))
    if a%2!=0:
        ans = "No"
        break
    T,X,Y = t,x,y
print(ans)