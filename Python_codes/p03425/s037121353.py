import itertools
n = int(input())
s = [input() for _ in range(n)]
a = [0,0,0,0,0]
for i in range(len(s)):
    if (s[i][0]=="M"):
        a[0] += 1
    elif (s[i][0]=="A"):
        a[1] += 1
    elif (s[i][0]=="R"):
        a[2] += 1
    elif (s[i][0]=="C"):
        a[3] += 1
    elif (s[i][0]=="H"):
        a[4] += 1

l = [0,1,2,3,4]
p = list(itertools.combinations(l, 3))
ans = 0
for i in range(len(p)):
    x,y,z = p[i][0],p[i][1],p[i][2]
    ans += a[x]*a[y]*a[z]
print(ans)