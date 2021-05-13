N = int(input())
V = list(map(int, input().split()))

V_ODD = [v for i,v in enumerate(V) if i%2==1]
V_EVEN = [v for i,v in enumerate(V) if i%2==0]

import collections

V_ODD_SORTED = sorted(list(zip(collections.Counter(V_ODD).values(), collections.Counter(V_ODD).keys())), reverse=True)
V_EVEN_SORTED = sorted(list(zip(collections.Counter(V_EVEN).values(), collections.Counter(V_EVEN).keys())), reverse=True)

ans_list = []

if V_ODD_SORTED[0][1] == V_EVEN_SORTED[0][1]:
    if len(V_ODD_SORTED) > 1:
        tmp = len(V)//2 - V_ODD_SORTED[1][0]
        tmp += len(V)//2 - V_EVEN_SORTED[0][0]
        ans_list.append(tmp)
        
    if len(V_EVEN_SORTED) > 1:
        tmp = len(V)//2 - V_ODD_SORTED[0][0]
        tmp += len(V)//2 - V_EVEN_SORTED[1][0]
        ans_list.append(tmp)

    if len(V_ODD_SORTED) == 1 and len(V_EVEN_SORTED) == 1:
        ans_list.append(len(V)//2)
        
else:
    tmp = len(V)//2 - V_ODD_SORTED[0][0]
    tmp += len(V)//2 - V_EVEN_SORTED[0][0]
    ans_list.append(tmp)
    
print(min(ans_list))