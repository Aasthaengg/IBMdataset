def f():
    return raw_input()
def f2():
    return raw_input().split()

dic = {}
n = int(f())
for i in range(n):
    c1, c2 = f2()
    if c1 == 'insert':
        dic[c2] = 548
    elif c1 == 'find':
        if dic.has_key(c2):
            print 'yes'
        else:
            print 'no'