s = input()
l = len(s)
ans = 0
for i in range(l):
    loc = 0
    idx = i 
    while s[idx] in ["A","C","G","T"] and idx<l:
        loc += 1
        idx += 1
        if idx>=l:
            break
    ans = max(ans,loc)
print(ans)