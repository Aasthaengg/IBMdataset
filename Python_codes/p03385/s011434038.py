s = list(input())
ans = 'Yes'
for i in ['a', 'b', 'c']:
    if i in s:
        continue
    ans = 'No'
print(ans)