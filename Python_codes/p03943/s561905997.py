A,B,C =map(int,input().split())
ls = [A,B,C]
ls.sort()
if ls[0] + ls[1] == ls[2]:
    print('Yes')
else:
    print('No')