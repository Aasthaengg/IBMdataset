N,K,Q = map(int,input().split())
Answer_List = {}
for i in range(Q):
    CA = int(input())
    if CA in Answer_List:
        Answer_List[CA] += 1 
    else:
        Answer_List[CA] = 1
 
Lose_Status = K - Q
if Lose_Status > 0:
    for j in range(N):
        print("Yes")
else:
    Standard = abs(Lose_Status) + 1
    for j in range(N):
        if j + 1 in Answer_List:
            if Answer_List[j + 1] >= Standard:
                print("Yes")
            else:
                print("No")
        else:
                print("No")
            
