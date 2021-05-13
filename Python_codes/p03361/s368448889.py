H, W = map(int, input().split())
s = ['.'+input()+'.' for _ in range(H)]
s.insert(0,'.'*(W+2))
s.append('.'*(W+2))
for i in range(1,H+1):
    for j in range(1,W+1):
        if s[i][j] == '#' and (s[i-1][j] + s[i][j-1:j+2] + s[i+1][j]).count('#') == 1:
            print('No')
            exit()
print('Yes')
