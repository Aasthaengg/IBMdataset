s = input()
s += 'q'
ans = ''
lst = []
for ss in s:
    if ss in ['A', 'C', 'G', 'T']:
        ans += ss
    else:
        lst.append(len(ans))
        ans = ''
print(max(lst))