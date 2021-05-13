ans = {}
t = input()
for i in range(len(t)):
    if t[i] not in ans:
        ans[t[i]] = i + 1

    for j in range(i+1, len(t)):
        if t[i] == t[j]:
            if t[i] in ans:
                ans[t[i]] = max(ans[t[i]], abs(j - i))
            else:
                ans[t[i]] = abs(j - i)
            
            break
    
        if j == len(t) - 1:
            ans[t[i]] = max(ans[t[i]], abs(j + 1 - i))


print(min(ans.values()) - 1)