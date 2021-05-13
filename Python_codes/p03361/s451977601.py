h,w=map(int,input().split())
s=[0]*h
for i in range(h):
    s[i] = input()

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if i != 0:
                if s[i-1][j] == '#':
                    continue
            if j != 0:
                if s[i][j-1] == '#':
                    continue
            if i != h-1:
                if s[i+1][j] == '#':
                    continue
            if j != w-1:
                if s[i][j+1] == '#':
                    continue
        else:
            continue
        print('No')
        exit()

print('Yes')