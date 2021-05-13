h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
for i in range(h):
    s[i].insert(w,0)
    s[i].insert(0,0)
s.insert(h,[0]*(w+2))
s.insert(0,[0]*(w+2))
x = '#'
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j] == x:
            if s[i-1][j] == x or s[i][j-1] == x or s[i][j+1] == x or s[i+1][j] == x:
                pass
            else:
                print('No')
                exit(0)

print('Yes')