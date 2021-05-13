s = input()
t = input()
n = len(s) - len(t) + 1
m = len(t)
ans = 0
for i in range(n):
    c = 0
    for j in range(m):
        if s[j+i] == t[j]:c+=1
    
    ans = max(c,ans)
print(m-ans)