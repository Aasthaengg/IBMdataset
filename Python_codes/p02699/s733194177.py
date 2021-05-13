sw=list(map(int, input().split()))
s=sw[0]
w=sw[1]

if w>=s:
    print('unsafe')
else:
    print('safe')
