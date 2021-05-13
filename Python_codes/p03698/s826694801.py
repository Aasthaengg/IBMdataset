s = list(input())
i = len(s)
s = list(set(s))
j = len(s)

if i != j:
    print('no')
else:
    print('yes')