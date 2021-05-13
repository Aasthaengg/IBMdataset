from collections import defaultdict
Poll_Dict = defaultdict(int)

N = int(input())

for _ in range(N):
    Poll_Dict[str(input())] += 1

Max_Number = max(Poll_Dict.values())    
Max_List = sorted([k[0] for k in Poll_Dict.items() if k[1] == Max_Number])

for i in Max_List:
    print(i)