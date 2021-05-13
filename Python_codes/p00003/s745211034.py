def pgr(x, y, z):
    if x**2 + y**2 == z**2: return True
    else: return False
    
while 1:
    try:
        n = input()
        for i in range(n):
            a,b,c = map(int, raw_input().split())
            if (pgr(a,b,c) or pgr(b,c,a) or pgr(c,a,b)): print 'YES'
            else: print 'NO'
        break
    except EOFError:
        break