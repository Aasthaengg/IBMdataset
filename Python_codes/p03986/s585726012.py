x = input()
ans = []

for i in x:
    if i == 'S':
        ans.append(i)
    else:
        if len(ans) == 0 or ans[-1] == 'T':
            ans.append(i)
        else:
            ans.pop()
print(len(ans))
