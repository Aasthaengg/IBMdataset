l = list(map(int, input().split()))
m = max(l)
l.remove(max(l))
s = sum(l)
if m == s:
    print('Yes')
else:
    print('No')