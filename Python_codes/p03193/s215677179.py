n, h, w = map(int, raw_input().split())
ans = 0
for i in range(n):
    l, r = map(int, raw_input().split())
    if l >= h and r >= w:
        ans += 1 
print ans