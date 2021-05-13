N,M = map(int,input().split())
L_list = []
R_list = []
for o in range(M):
    L,R = map(int,input().split())
    L_list.append(L)
    R_list.append(R)
L_max = max(L_list)
R_min = min(R_list)
    
if L_max <= R_min:
    ans = R_min - L_max + 1
else:
    ans = 0
print(ans)