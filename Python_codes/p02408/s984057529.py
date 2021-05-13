
x = input()
mark = []
num = []
for i in xrange(x):
    inp = raw_input().split()
    inp[1] = int(inp[1])
    mark.append(inp)

trump = ["S","H","C","D"]
for i in xrange(4):
    for j in xrange(13):
        tako = [str(trump[i]), int(j + 1)]
        p = len(mark)
        for k in range(p):
            if tako == mark[k]:
                del mark[k]
                break
            if k == (p - 1):
                mark.append(tako)
for i in xrange(len(mark)):
    print mark[i][0], mark[i][1]