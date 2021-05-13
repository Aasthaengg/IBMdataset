H, W = map(int, input().split())
s = []
for i in range(H):
    s.append(input()+'.')
s.append("."*(W+1))
# print(s)

flug = True
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            if not (s[i+1][j] == '#' 
                    or s[i-1][j] == '#' 
                    or s[i][j+1] == '#' 
                    or s[i][j-1] == '#'):
                flug = False
if flug:
    print("Yes")
else:
    print("No")
