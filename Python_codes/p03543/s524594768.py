n = input()
l = [int(x) for x in list(str(n))]

if l[0]==l[1]==l[2] or l[1]==l[2]==l[3]:
    print('Yes')
else:
    print('No')