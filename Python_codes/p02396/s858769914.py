# coding=utf-8

i = 1
while True:
    x = int(raw_input().rstrip())
    if x:
        print "Case {0}: {1}".format(i, x)
        i += 1
    else:
        break