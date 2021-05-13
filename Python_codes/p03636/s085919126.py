
s = list(input())
ans = []
ans.append(s[0])
ans.append(str((len(s)-2)))
ans.append(s[-1])

print("".join(ans))
