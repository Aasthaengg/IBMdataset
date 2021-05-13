s = input()
rcount = 0
ans = [0]*len(s)
for i in range(len(s)-1):
    if s[i] == "R" and s[i+1] == "R":
        rcount += 1
    elif s[i] == "R" and s[i+1] == "L":
        rcount += 1
        ans[i+1] += rcount // 2
        ans[i] += rcount - rcount//2
        rcount = 0
    else:
        rcount = 0
lcount = 0
for i in range(len(s)-1, 0, -1):
    if s[i] == "L" and s[i-1] == "L":
        lcount += 1
    elif s[i] == "L" and s[i-1] == "R":
        lcount += 1
        ans[i-1] += lcount // 2
        ans[i] += lcount - lcount//2
        lcount = 0
    else:
        lcount = 0
for i in range(len(ans)):
    ans[i] = str(ans[i])
print(" ".join(ans))