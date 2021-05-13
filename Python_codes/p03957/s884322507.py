s = input()
C = False

ans = 'No'
for i in s:
    if i == 'C':
        C = True

    if i == 'F' and C:
        ans = 'Yes'
        break
print(ans)
