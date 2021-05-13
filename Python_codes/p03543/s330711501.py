N = input()
if N[:3].count(N[0]) == 3 or N[1:].count(N[1]) == 3:
    print('Yes')
else:
    print('No')