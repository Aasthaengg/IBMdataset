N=int(input())
V=list(map(int,input().split()))

from collections import Counter
V_1=V[::2]
V_2=V[1::2]

V_1_counter=Counter(V_1).most_common()
V_2_counter=Counter(V_2).most_common()
# print(V_1_counter,V_2_counter)

V_1_max_1 = V_1_counter[0]
V_1_max_2=(0,0)
if len(V_1_counter)>1:
    V_1_max_2 = V_1_counter[1]
    
V_2_max_1=V_2_counter[0]
V_2_max_2=(0,0)
if len(V_2_counter)>1:
    V_2_max_2 = V_2_counter[1]
    
if V_1_max_1[0] != V_2_max_1[0]:
    ans = N-V_1_max_1[1]-V_2_max_1[1]
    
else:
    ans=N-max(V_1_max_1[1]+V_2_max_2[1],V_1_max_2[1]+V_2_max_1[1])
    
print(ans)