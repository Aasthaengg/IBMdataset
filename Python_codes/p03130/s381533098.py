a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

load = [a1, b1, a2, b2, a3, b3]
load_dict = dict()
for i in range(6):
    if load[i] in load_dict:
        load_dict[load[i]] += 1
    else:
        load_dict[load[i]] = 1
        
if max(load_dict.values()) >= 3 or len(load_dict) <= 3:
    print("NO")
else:
    print("YES")