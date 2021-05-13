S = input()

r = 0
l = 0
ans = 0
val = 0
for i in range(len(S)):
    if(S[i] == "<"):
        if(l == 1):
            r = 1
            if(val > l):
                ans += val
                val = 0
                l = 0
            else:
                ans += l
                l = 0
        elif(l > 1):
            if(val > l):
                ans += (l*(l+1))//2+(val-l)
                l = 0
                r = 1
                val = 0
            else:
                ans += (l*(l+1))//2
                l = 0
                r = 1
                val = 0
        else:
            r += 1
    else:
        if(r):
            ans += (r*(r-1))//2
            val = r
            l = 1
            r = 0
        else:
            l += 1
if(l):
    if(l == 1):
        if(val > l):
            ans += val
        else:
            ans += l
    else:
        if(val > l):
            ans += (l*(l+1))//2+(val-l)
        else:
            ans += (l*(l+1))//2
else:
    ans += (r*(r+1))//2
print(ans)