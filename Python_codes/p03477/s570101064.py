ABCD=list(map(int,input().split(' ')))
l,r=sum(ABCD[:2]),sum(ABCD[2:])
if l>r:
    print('Left')
elif l==r:
    print('Balanced')
else:
    print('Right')