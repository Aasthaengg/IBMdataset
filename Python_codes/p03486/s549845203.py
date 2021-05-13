s = sorted(input())
t = sorted(input(), reverse=True)

if s == t:
    print('No')

else:
    a = sorted([s, t])
    if a[0] == s:
        print('Yes')

    if a[0] == t:
        print('No')