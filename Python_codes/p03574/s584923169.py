h, w = map(int,input().split())

dx = [1,1,1,0,-1,-1,-1,0]
dy = [0,1,-1,1,0,1,-1,-1]
ans = [[0] * (w + 2) for _ in range(h + 2)]

s = [input() for _ in range(h)]
for i in range(h):
    s[i] = '.' + s[i] + '.' 
s = ['.' * (w + 2)] + s + ['.' * (w + 2)] 

for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == '.':
            for A in range(8):
                if(s[i + dy[A]][j + dx[A]]=='#'):
                    ans[i][j] += 1
            

for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == '.':
            print(ans[i][j],end='')
        else:
            print('#',end='')
    print()