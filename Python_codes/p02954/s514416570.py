s = str(input())
ls = [0]*len(s)
r = 0
l = 0
ind = 0
if s[0] == "R":
    r = 1
else:
    l = 1
for i in range(1,len(s)):
    if s[i-1] == "L" and s[i] == "R":
        ls[ind] = (l - l//2) + r//2
        if ind > 0:
            ls[ind-1] = (r - r//2) + l//2
        l = 0
        r = 1
    elif s[i-1] == "R" and s[i] == "L":
        ind = i
        l += 1
    else:
        if i == len(s)-1:
            if s[i] == "L":
                l += 1
                ls[ind] = (l - l//2) + r//2
                if ind > 0:
                    ls[ind-1] = (r - r//2) + l//2
                r = 0
                l = 0
            else:
                r += 1
                ls[-1] = r
                r = 0
        else:
            if s[i] == "R":
                r += 1
            else:
                l += 1
if r != 0 and l != 0:
    ls[ind] = (l - l//2) + r//2
    if ind > 0:
        ls[ind-1] = (r - r//2) + l//2
elif r != 0:
    ls[-1] = r
print(*ls)