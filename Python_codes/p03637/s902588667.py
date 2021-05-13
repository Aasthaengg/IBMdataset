n,*aa = map(int, open(0).read().split())

odd = sum([a%2 for a in aa])
quad = sum([a%4==0 for a in aa])

if odd <= quad or (odd == quad + 1 and odd+quad == len(aa)):
    print('Yes')
else:
    print('No')