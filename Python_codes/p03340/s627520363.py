n = int(input())
ai = [int(i) for i in input().split()]

ans = 0
s = 0
x = 0

r = 0
            
for l in range(n):
    while r <= n-1 and s+ai[r] == x^ai[r]:
        s += ai[r]
        x ^= ai[r]
        r += 1
    ans += (r-l)
    
    if l == r:
        r += 1
    else:
        s -= ai[l]
        x ^= ai[l]
        
print(ans)