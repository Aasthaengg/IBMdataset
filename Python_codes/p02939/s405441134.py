s = input()
n = len(s)
ans = [s[0]]
idx = 1
while idx < n:
    if s[idx] != ans[-1]:
        ans.append(s[idx])
        idx += 1
    else:
        if idx < n-1:
            ans.append(s[idx] + s[idx+1])
            idx += 2
        else:
            break

#print(ans)
print(len(ans))