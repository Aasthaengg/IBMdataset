n = input()
state = 0
for k in range(448):
    if n * 2 == k * (k + 1):
        state = 1
        print "Yes"
        print k + 1
        break
if state == 1:
    arr = [[0 for j in range(k)] for i in range(k + 1)]
    number = 1
    for p in range(k):
        temp = number
        for s in range(p+1):
            # print "p", p, "s", s, "number", number
            arr[s][p] = number
            number += 1
        number = temp
        for t in range(p+1):
            # print "p+1", p+1, "t", t, "number", number
            arr[p+1][t] = number
            number += 1

    for a in arr:
        print len(a),
        for b in a:
            print b,
        print
else:
    print "No"
