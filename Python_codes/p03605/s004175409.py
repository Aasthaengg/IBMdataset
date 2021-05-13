N = str(input())

ans = 'No'

for a in N:
    if a == '9':
        ans = 'Yes'
        break
    else:
        ans = 'No'

print(ans)
