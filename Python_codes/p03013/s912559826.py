#https://atcoder.jp/contests/abc129/tasks/abc129_c
N,M = map(int,input().split())
Danger_List = []
Route_List = [[] for i in range(N+1)]
for i in range(M):
    Route_List[int(input())] = 0
        
Route_List[0] = 1

for i in range(1,N+1):
    if Route_List[i] != 0:
        if i == 1:
            Route_List[i] = 1
        else:
            Route_List[i] = Route_List[i-1] + Route_List[i-2]

    
    
        
print(Route_List[-1] % 1000000007)