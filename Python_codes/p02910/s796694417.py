s = input()

ans = 'Yes'
for i, si in enumerate(s):
    if ((i % 2 == 0) and (si == 'L')) or ((i % 2 == 1) and (si == 'R')):
        ans = 'No'
        break
print(ans)
