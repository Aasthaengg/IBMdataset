Q = int(input())
l = []
r = []
for i in range(Q):
    a, b = map(int, input().split())
    l.append(a)
    r.append(b)
    
x =[True]*((10**5)+1)
x[0] = False
x[1] = False
s = [0, 0, 0]

for i in range(4, (10**5)+1, 2):
    x[i] = False

for j in range(3, (10**5)+1):
    if x[j] == False:
        s.append(s[-1])
        continue
    for k in range(2*j, (10**5)+1, j):
        x[k] = False
    if x[(j+1)//2] == True:
        s.append(s[-1]+1)
    else:
        s.append(s[-1])

for i in range(Q):
    print(s[r[i]]-s[l[i]-1])