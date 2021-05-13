alpha2num = lambda c: ord(c) - ord('a') + 1
c = [0] * 27

h, w = map(int, input().split())
s = [[] for _ in range(h)]
for i in range(h):
    s[i] = list(input())
    for j in range(w):
        c[alpha2num(s[i][j])] += 1

if h % 2 == 0 and w % 2 == 0:
    flag = 1
elif h % 2 == 0 and w % 2 == 1:
    flag = 2
elif h % 2 == 1 and w % 2 == 0:
    flag = 3
elif h % 2 == 1 and w % 2 == 1:
    flag = 4


#print(c)
c1 = 0
c2 = 0
for i in range(len(c)):
    if c[i] % 4 == 1:
        c1 += 1
    elif c[i] % 4 == 2:
        c2 += 1
    elif c[i] % 4 == 3:
        c1 += 1
        c2 += 1

#print(c1, c2)

ans = 'No'
if flag == 1:
    if c1 == c2 == 0:
        ans = 'Yes'
elif flag == 2:
    if c1 == 0 and c2 <= h//2:
        ans = 'Yes'
elif flag == 3:
    if c1 == 0 and c2 <= w//2:
        ans = 'Yes'  
else:
    if c1 == 1 and c2 <= h//2 + w//2:
        ans = 'Yes'

print(ans)