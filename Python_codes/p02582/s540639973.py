S = input()

ans = 0
tmp = 0
for ch in S:
    if ch == 'R':
        tmp += 1
        ans = max(ans, tmp)
    else:
        ans = max(ans, tmp)
        tmp = 0    
print(ans)