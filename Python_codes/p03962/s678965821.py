a, b, c = map(int, input().split())
ans = 1

if(a != b and a != c):
    ans += 1
if(b != c):
    ans += 1
    
print(ans)