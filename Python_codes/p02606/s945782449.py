L, R, d = map(int, input().split())

l = L // d
r = R // d

ans = r - l
if L % d == 0 and R % d == 0:
    ans += 1
    
print(ans)
