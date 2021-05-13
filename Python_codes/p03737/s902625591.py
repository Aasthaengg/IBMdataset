s = list(input().split())
    
a = []
a.append(s[0][0].upper())
a.append(s[1][0].upper())
a.append(s[2][0].upper())
print(*a, sep='')