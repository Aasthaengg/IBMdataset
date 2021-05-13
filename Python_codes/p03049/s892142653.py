n = int(input())
a = 0
b = 0
ba = 0
ans = 0
for i in range(n):
    s = input()
    ans += s.count('AB')
    if s[0] == "B" and s[-1] == "A":
        ba += 1
    elif s[0] == "B":
        b += 1
    elif s[-1] == "A":
        a += 1
        
if ba == 0:
    ans += min(a,b)
elif ba != 0:
    if a == 0 and b == 0:
        ans += ba-1
    else:
        ans += ba + min(a,b)
print(ans)