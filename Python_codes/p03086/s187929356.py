s = input()

ans = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        tmp = s[i:j+1]
        if set(list(tmp)) <= set(["A","C","G","T"]):
            ans = max(ans,len(tmp))
print(ans)