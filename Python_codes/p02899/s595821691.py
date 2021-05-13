N = int(input())
N_List =list(map(int,input().split()))
ans = [0] * N
for i in range(N):
    s = N_List[i]   
    ans[s-1] = i+1  
print(*ans)