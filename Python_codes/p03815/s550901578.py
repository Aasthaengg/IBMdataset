x = int(input())
ans = (x//11) * 2

y = x % 11

if 6 < y:
    ans += 2
elif 1 <= y <= 6:
    ans += 1
    
print(ans)