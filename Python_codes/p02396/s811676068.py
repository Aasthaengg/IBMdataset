i = 1
flag = True
while flag:
    
    x = int(raw_input())
    if x != 0:
        print 'Case %s: %s' % (i,x)
        i += 1
    else:
        flag = False