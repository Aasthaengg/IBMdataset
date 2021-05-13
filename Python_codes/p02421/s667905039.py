n = int(input())
t_co = h_co = 0

for i in range(n):
    t_str, h_str = list(map(str, input().split()))
    
    if t_str > h_str:
        t_co += 3
    
    elif h_str == t_str:
        t_co += 1
        h_co += 1
    else:
        h_co += 3
        
print(t_co, h_co)

