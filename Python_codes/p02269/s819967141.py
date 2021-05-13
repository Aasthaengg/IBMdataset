n=input()

d=set()
for x in xrange(n):
    cmd, st = map(str, raw_input().split())
    
    if cmd == "insert":
        d.add(st)
    elif cmd == "find":
        print 'yes' if st in d else 'no'