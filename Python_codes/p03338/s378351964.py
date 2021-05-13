n = int(input())
s = input()

ans = 0
for i in range(1, n):
    left = list(s[:i])
    right = list(s[i:])
    
    t = 0
    for j in set(left):
        if j in right:
            t += 1
    
        ans = max(ans, t)
        
print(ans)