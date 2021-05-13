n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    aa, bb = map(int,input().split())
    a[n-i-1] = aa
    b[n-i-1] = bb
ans = 0

for i,aa in enumerate(a):
    cnt = (aa + ans) % b[i]
    if cnt != 0:
        cnt = b[i] - cnt
    
    ans += cnt
print(ans)
