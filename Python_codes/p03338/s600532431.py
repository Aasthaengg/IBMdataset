n = int(input())
s = input()

# print(s)
max_count = 0
for i in range(len(s)):
    ss = "abcdefghijklmnopqrstuvwxyz"
    x_dict = {}
    y_dict = {}
    for c in ss:
        x_dict[c] = 0
        y_dict[c] = 0
        
    # print(i)
    
    x = s[:i]
    y = s[i:]
    # print(f"{x} {y}")
    
    for xx in x:
        x_dict[xx] += 1
        
    for yy in y:
        y_dict[yy] += 1
    
    # print(x_dict)
    # print(y_dict)
    
    count = 0
    for c in ss:
        # print(f"{x_dict[c]} {y_dict[c]}")
        if x_dict[c] > 0 and y_dict[c] > 0:
            # print(f"{x_dict[c]} {y_dict[c]}")
            count += 1
    # print(count)
    max_count = max(max_count, count)
        
print(max_count)