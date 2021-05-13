L = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for x in range(int(input())):
    n = raw_input().split()
    b = int(n[0])
    f = int(n[1])
    r = int(n[2])
    v = int(n[3])

    L[b-1][f-1][r-1] += v

for i in L:
    for j in i:
        print (" {}" * 10).format(*j)
    if i is not L[-1] :print "#" * 20