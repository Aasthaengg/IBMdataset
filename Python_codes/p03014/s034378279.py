h,w = map(int,input().split())
s = [0]*h
for i in range(h):
    s[i] = list(input())
ver = [[0 for j in range(w)] for i in range(h)]
hol = [[0 for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            pass
        elif j >= 1 and hol[i][j-1] != 0:
            hol[i][j] = hol[i][j-1]
        else:
            for k in range(2000):
                if j+k+1 >= w:
                    break
                if s[i][j+k+1] == "#":
                    break
            hol[i][j] = k+1
            
for j in range(w):
    for i in range(h):
        if s[i][j] == "#":
            pass
        elif ver[i][j] == 0 and i >= 1 and ver[i-1][j] != 0:
            ver[i][j] = ver[i-1][j]
        else:
            for k in range(2000):
                if i+k+1 >= h:
                    break
                elif s[i+k+1][j] == "#":
                    break
            ver[i][j] = k+1

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, hol[i][j] + ver[i][j] - 1)
print(ans)