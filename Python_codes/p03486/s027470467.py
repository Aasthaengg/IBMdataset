s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
s1 = ''.join(s)
t1 = ''.join(t)
ls = [s1,t1]
ls1 = sorted(ls)
if s1 == t1:
    print('No')
elif ls == ls1:
    print('Yes')
else:
    print('No')