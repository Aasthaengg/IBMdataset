T = str(input())

ans = []
for i in T:
    if i == '?':
        ans.append('D')
    else:
        ans.append(i)

print(''.join(ans))
