S = input()
ans = 'Yes'
if len(S)%2:
    ans = 'No'
else:
    for i, c in enumerate(S):
        if i%2 and c!='i':
            ans = 'No'
            break
        elif i%2 == 0 and c!='h':
            ans = 'No'
            break
print(ans)
