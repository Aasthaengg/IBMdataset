n = int(raw_input())
dic = {}

for i in xrange(n):
    a, b = raw_input().split()
    if a == "insert":
        dic[b] = True
    elif a == "find":
        if b in dic:
            print "yes"
        else:
            print "no"