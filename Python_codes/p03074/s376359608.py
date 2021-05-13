n,k = map(int,input().split())
s = list(input())
if s[0] == "0":
    x_1 = [[0,0]]
else:
    x_1 = []
i = 0
while i < n:
    j = 0
    y_s = i
    while s[i] == s[i+j]:
        if i+j >= n-1:
            j += 1
            break
        j += 1
    y_e = i+j
    if s[i] == "1":
        x_1.append([y_s,y_e])
    i += j
if s[-1] == "0":
    x_1.append([n,n])
ans = 0
i = 0
if k >= len(x_1):
    ans = n
while i < n:
    if i+k >= len(x_1):
        break
    ans = max(ans,x_1[i+k][1]-x_1[i][0])
    i += 1
print(ans)