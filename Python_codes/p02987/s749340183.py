a=list(input())
b=sorted(a)
if b[0]==b[1] and b[2]==b[3] and b[1]!=b[2]:
    print('Yes')
else:
    print('No')