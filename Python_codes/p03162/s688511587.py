# https://atcoder.jp/contests/dp/tasks/dp_c
N = int(input())
Max_List=[]
N_List=[i for i in range(3)]
for i in range(N):
    Current_List=list(map(int,input().split())) 
    if i == 0:
        Max_List.append(Current_List)
    else:
        Current_Max_List = []
        Search_List=Max_List[i-1]
        for j in range(3):
            Current_Search_List=Search_List[1:3]
            Current_Max_List.append(max(Current_Search_List)+Current_List[j])
            Search_List.append(Search_List[0])
            del Search_List[0]
        Max_List.append(Current_Max_List)
        
    
print(max(Max_List[-1]))