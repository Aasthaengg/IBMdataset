def check(s):
    an = True
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            an = False
    return an    
a,b = map(int, input().split())
ans = 0
for i in range(a,b+1):
    l = str(i)
    l2 = list(l)
    if check(l2):
        ans += 1
print(ans)