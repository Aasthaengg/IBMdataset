n = int(input())
s = list(input())

def solve(x,y):

    sx = set(x)
    sy = set(y)
    s_com = sx & sy
    return len(s_com)

ans = 0
for i in range(n):
    x = s[:i]
    y = s[i:]
    ans = max(ans,solve(x,y))

print(ans)



