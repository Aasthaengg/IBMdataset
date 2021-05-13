input()
s = input()
m = 0

for i in range(1,len(s)):
    f = s[:i]
    g = s[i:]
    
    x = set(f)
    count = 0
    
    for j in x:
        if j in g:
            count = count+1
    m = max(count,m)

print(m)