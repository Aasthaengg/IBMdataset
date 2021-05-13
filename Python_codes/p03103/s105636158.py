N,M = map(int,input().split())
Shop_List = [list(map(int,input().split())) for i in range(N)]
Shop_List = sorted(Shop_List, key=lambda x:x[0])
Number_Counter = 0
Yen_Counter = 0
for i in range(N):
    if Number_Counter + Shop_List[i][1] <= M:
        Number_Counter += Shop_List[i][1]
        Yen_Counter += Shop_List[i][0]*Shop_List[i][1]
    elif Number_Counter + Shop_List[i][1] > M:
        Yen_Counter += (M-Number_Counter)*Shop_List[i][0]
        Number_Counter = M
    elif Number_Counter == M:
        break

print(Yen_Counter)
