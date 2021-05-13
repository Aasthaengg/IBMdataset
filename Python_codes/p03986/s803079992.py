X = input()
ans = []
for x in X:
    if x == 'S':
        ans.append(x)
    else:
        if len(ans) != 0:
            if ans[-1] == 'S':
                ans.pop()
            else:
                ans.append(x)
        else:
            ans.append(x)
print(len(ans))
