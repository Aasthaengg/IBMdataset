r,d,x0 = map(int,input().split())
ans = [0] * 11
ans[0] = x0
for i in range(10):
    ans[i + 1] = r * ans[i] - d 
    print(ans[i + 1]) 
