h,w = map(int,input().split())
c = []
for i in range(10):
    tmp = list(map(int,input().split()))
    c.append(tmp)
    
for i in range(10): ##経由する頂点
    for j in range(10): ## 始点
        for k in range(10): ## 終点
            c[j][k] = min(c[j][k] , c[j][i] + c[i][k])
            
            
num_list = [0]*10
for i in range(h):
    tmp = list(map(int,input().split()))
    for j in tmp:
        if j != -1:
            num_list[j] += 1
ans = 0      
for i in range(len(num_list)):
    ans += c[i][1]*num_list[i]
    
print(ans)