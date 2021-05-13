s = input()
# print(s)

ans = 0
count = 0
for c in s:
    # print(c)
    
    if c in ['A', 'C', 'G', 'T']:
        count += 1
    else:
        count = 0
        
    # print(ans)
    ans = max(ans, count)
    
print(ans)