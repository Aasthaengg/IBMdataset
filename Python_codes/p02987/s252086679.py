s = input()
ans = 'Yes'
for c in s:
    if s.count(c) != 2:
        ans = 'No'
        break
print(ans)
