se = set([])
n = int(raw_input())
for i in range(n):
    order, string = raw_input().split()
    if order == 'insert':
        se.add(string)
    elif order == 'find':
        if string in se:
            print 'yes'
        else:
            print 'no'