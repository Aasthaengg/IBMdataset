n = int(input())
s = list(str(input()))

score = 0

for i in range(1,n-1):
    if s[i] == 'R':

        g = 0
        g_l = []
        for j in range(i):
            if s[j] == 'G':
                g += 1
                g_l.append(i-j)
        b = 0         
        b_l = []
        for j in range(i,n):
            if s[j] == 'B':
                b += 1
                b_l.append(j-i)
                
        common = set(g_l) & set(b_l)
        score += b*g - len(common)

for i in range(1,n-1):
    if s[i] == 'R':

        g = 0
        g_l = []
        for j in range(i):
            if s[j] == 'B':
                g += 1
                g_l.append(i-j)
        b = 0         
        b_l = []
        for j in range(i,n):
            if s[j] == 'G':
                b += 1
                b_l.append(j-i)
                
        common = set(g_l) & set(b_l)
        score += b*g - len(common)

for i in range(1,n-1):
    if s[i] == 'G':

        g = 0
        g_l = []
        for j in range(i):
            if s[j] == 'R':
                g += 1
                g_l.append(i-j)
        b = 0         
        b_l = []
        for j in range(i,n):
            if s[j] == 'B':
                b += 1
                b_l.append(j-i)
                
        common = set(g_l) & set(b_l)
        score += b*g - len(common)

for i in range(1,n-1):
    if s[i] == 'G':

        g = 0
        g_l = []
        for j in range(i):
            if s[j] == 'B':
                g += 1
                g_l.append(i-j)
        b = 0         
        b_l = []
        for j in range(i,n):
            if s[j] == 'R':
                b += 1
                b_l.append(j-i)
                
        common = set(g_l) & set(b_l)
        score += b*g - len(common)

for i in range(1,n-1):
    if s[i] == 'B':

        g = 0
        g_l = []
        for j in range(i):
            if s[j] == 'R':
                g += 1
                g_l.append(i-j)
        b = 0         
        b_l = []
        for j in range(i,n):
            if s[j] == 'G':
                b += 1
                b_l.append(j-i)
                
        common = set(g_l) & set(b_l)
        score += b*g - len(common)

for i in range(1,n-1):
    if s[i] == 'B':

        g = 0
        g_l = []
        for j in range(i):
            if s[j] == 'G':
                g += 1
                g_l.append(i-j)
        b = 0         
        b_l = []
        for j in range(i,n):
            if s[j] == 'R':
                b += 1
                b_l.append(j-i)
                
        common = set(g_l) & set(b_l)
        score += b*g - len(common)
        
print(score)
