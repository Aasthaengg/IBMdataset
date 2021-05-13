ip=map(int,raw_input().split())
if ip[0]==ip[1]:
    print 'a == b'
elif ip[0]>ip[1]:
    print 'a > b'
else:
    print 'a < b'