##https://atcoder.jp/contests/dp/tasks/dp_a 
N,K = map(int,input().split())
Place_Height_List = list(map(int,input().split()))  
Min_List = [0,abs(Place_Height_List[1]-Place_Height_List[0])]

for i in range(2,len(Place_Height_List)):
    Current_Step_Min = 10 ** 9
    for j in range(1,min(i,K)+1):
        Current_Step = Min_List[i - j] + abs(Place_Height_List[i] - Place_Height_List[i - j])
        if Current_Step_Min > Current_Step:
            Current_Step_Min = Current_Step
        
    Min_List.append(Current_Step_Min)
print(Min_List[-1])