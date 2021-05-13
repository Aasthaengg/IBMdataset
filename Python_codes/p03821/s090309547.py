n = int(input())
lis = [list(map(int,input().split())) for i in range(n)]
cnt = 0
for i in range(n-1,-1,-1):
    cnt += -(lis[i][0] + cnt)%lis[i][1]
    
print(cnt)