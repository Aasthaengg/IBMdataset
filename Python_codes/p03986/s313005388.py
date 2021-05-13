s=input()

s=list(s)

ans = ['G']

for i in s:
    if i == 'S':
        ans.append(i)
    else:
        if ans[-1] == 'S':
            ans.pop(-1)
        else:
            ans.append(i)
print(len(ans)-1)