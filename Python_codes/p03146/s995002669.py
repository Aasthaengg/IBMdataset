s = int(input())
ans = []
i = 1
while s not in ans:
    ans.append(s)
    if s % 2 == 0:
        s //= 2
    else:
        s = 3*s + 1
    i += 1
    
print(i)