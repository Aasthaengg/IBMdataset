s = input()
n = len(s)

t = []
for a in s:
    if a != "x":
        t.append(a)
t = "".join(t)
m = len(t)

sw = 1
for i in range(m//2):
    if t[i] == t[-1-i]:
        pass
    else:
        sw = 0
        
if sw == 0:
    ans = -1
else:
    ans = 0
    i,j = 0,0
    while i+j<n:
        if s[i] == s[-1-j]:
            i += 1
            j += 1
        elif s[i] == "x":
            i += 1
            ans += 1
        elif s[-1-j] == "x":
            j += 1
            ans += 1
            
        else:
            ans = -float("Inf")
            
print(ans)