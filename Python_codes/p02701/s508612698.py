N = int(input())
M_Dict = {}
for i in range(N):
    Current_M = str(input())
    if Current_M in M_Dict:
        M_Dict[Current_M] += 1
    else:
        M_Dict[Current_M] = 1
        

print(len(M_Dict))
