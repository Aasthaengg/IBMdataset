s = input()

if 'C' in s and 'F' in s:
    c_index = s.index('C')
    f_index = s.rindex('F')
    if c_index < f_index:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    ans = 'No'

print(ans)