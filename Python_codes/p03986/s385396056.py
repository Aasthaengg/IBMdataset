s = input()
n = len(s)
ans = []
for i in range(n):
    if s[i] == "S":
        ans.append(s[i])
    else:
        if ans == [] or ans[-1] != "S":
            ans.append(s[i])
        else:
            ans.pop()
print(len(ans))