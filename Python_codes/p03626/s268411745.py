n=int(input())
l1=[str(x) for x in input()]
l2=[str(x) for x in input()]

if l1[0]==l2[0]:
    pat=3
    typ='lon'
else:
    pat=6
    typ='lat'
for i in range(1,n):
    if l1[i]!=l1[i-1]:
        if typ=='lon':
            if l1[i]==l2[i]:
                pat *= 2
            else:
                pat *= 2
                typ='lat'
        else:
            if l1[i]==l2[i]:
                typ='lon'
            else:
                pat *= 3
print(pat%(10**9+7))