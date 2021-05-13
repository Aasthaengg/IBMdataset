x = int(input())
 
ans = x//11*2
t = x%11
if t > 6: 
    ans += 2
elif t > 0:
    ans += 1
print(ans)