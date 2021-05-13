a,b = map(int,input().split())
if min(a,b)*2+(max(a,b)-min(a,b))*2<=16:
    print('Yay!')
else:
    print(':(')