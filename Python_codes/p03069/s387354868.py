n = int(input())
s = input()
ans = 0
c = 0
for i in range(n):
    if s[i] == "#":
        c += 1
    else:
        if c >= 1:
            ans += 1
            c -= 1
    
print(ans)