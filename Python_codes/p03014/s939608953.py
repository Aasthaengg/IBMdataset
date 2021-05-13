h,w = map(int,input().split()) 
s = [0 for i in range(h)]
s1 = [[-1 for i in range(w)]for j in range(h)]
s2 = [[-1 for i in range(w)]for j in range(h)]
ans = 0
for i in range(h):
    s[i] = list(input())
for i in range(h):
    p = 0
    d = [-1]
    for j in range(w):
        if s[i][j] == '#':
            d.append(j)
    d.append(w)
    for j in range(w):
        if s[i][j] == '.':
            s1[i][j] = d[p+1]-d[p]-1
        else:
            p += 1
for j in range(w):
    p = 0
    d = [-1]
    for i in range(h):
        if s[i][j] == '#':
            d.append(i)
    d.append(h)
    for i in range(h):
        if s[i][j] == '.':
            s2[i][j] = d[p+1]-d[p]-1
        else:
            p += 1       
for i in range(h):
    for j in range(w):
        ans =  max(ans,s1[i][j] + s2[i][j])

        
        
print(ans-1)