def check(s):
    l=len(s)
    if l%2 :
        return 0
    for i in range(l//2):
        if s[i]!=s[i+l//2]:
            return 0
    return 1        

s = input()
ans = 0
for i in range(1,len(s)):
    if check(s[:len(s)-i]) :
        ans = len(s)-i
        break
print(ans)
