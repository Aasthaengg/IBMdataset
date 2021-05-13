n,m,x,y = map(int,input().split())
x_list = list(map(int,input().split()))
x_max = max(x_list)
y_list = list(map(int,input().split()))
y_min = min(y_list)
ans = "War"
for i in range(x+1,y+1):
    if x_max < i <= y_min:
        ans = "No War"
        break
print(ans)