N = int(input())
N_List = list(map(int,input().split()))
ans = 0
cans = 0
for i in range(1,N):
    if N_List[i] <= N_List[i-1]:
        cans += 1
    if cans > ans:
        ans = cans
    if N_List[i] > N_List[i-1]:
        cans = 0
    
print(ans)