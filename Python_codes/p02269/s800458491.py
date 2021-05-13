n = int(raw_input())
d = set()
for i in range(n):
    p,q = map(str,raw_input().split())
    if p == "insert":
        d.add(q)
    elif p == "find":
        if(q in d):
            print "yes"
        else:
            print "no"