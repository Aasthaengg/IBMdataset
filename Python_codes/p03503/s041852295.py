import sys
input = sys.stdin.readline
n = int(input())
f = [list(map(int,input().split()))for i in range(n)]
p = [list(map(int,input().split()))for i in range(n)]
ans = -float('inf')
for i in range(1,2**10):
    bin = format(i,'b').zfill(10)
    c = [0]*n
    for j in range(n):
        for k in range(10):
            if bin[k] == '1' and f[j][k] == 1:
                c[j] += 1
    r = 0
    for i in range(n):
        r += p[i][c[i]]
    ans = max(ans, r)
print(ans)
