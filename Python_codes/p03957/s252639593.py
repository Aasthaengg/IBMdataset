s = input()
ans = 'No'
if 'C' in s:
    if 'F' in ''.join(s.split('C')[1:]):
        ans = 'Yes'
print(ans)