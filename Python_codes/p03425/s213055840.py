import itertools
N = int(input())
M_Dict = {"M":0,"A":0,"R":0,"C":0,"H":0}
for i in range(N):
    moji = str(input())
    if moji[0] in M_Dict.keys():
        M_Dict[moji[0]] += 1
M_Dict = {k: v for k, v in M_Dict.items() if v != 0}    
if len(M_Dict) < 3:
    ans = 0
else:
    ans = 0
    for k in itertools.combinations(list(M_Dict.keys()),3):
        ans += int(M_Dict[k[0]]) * int(M_Dict[k[1]]) * int(M_Dict[k[2]])
    
print(ans)    