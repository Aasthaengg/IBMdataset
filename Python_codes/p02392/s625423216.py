str = raw_input()
list = map(int, str.split())

if list[0]<list[1]<list[2]:
    print 'Yes'
else:
    print 'No'