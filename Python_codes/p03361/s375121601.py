H, W = map(int, input().split())
s_a = []
for _ in range(H):
    s = list(input())
    s_a.append(s)

check_list = [(0,1),(0,-1),(1,0),(-1,0)]

def check(i,j):
    for x,y in check_list:
        try: 
            if s_a[i+x][j+y] == '#':
                return True
        except:
            continue
    return False

ans = 'Yes'
for i in range(H):
    for j in range(W):
        if s_a[i][j] == '#':
            if check(i,j):
                continue
            else:
                ans = 'No'
                break
print(ans) 