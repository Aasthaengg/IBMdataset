x = input()
n = len(x)
ans = []
for i in range(n):
    if x[i] == 'S':
        ans.append(x[i])
    else:
        if len(ans) > 0:
            if ans[-1] == 'S':
                ans.pop()
            else:
                ans.append(x[i])
        else:
            ans.append(x[i])
    # print(ans)

print(len(ans))