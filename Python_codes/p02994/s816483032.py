n, l = map(int, input().split())
a_l = [ l+i for i in range(n) ]

if 0 in a_l:
    print(sum(a_l))
elif a_l[0] < 0 :
    print(sum(sorted(a_l, reverse=True)[1:]))
else:
    print(sum(sorted(a_l)[1:]))