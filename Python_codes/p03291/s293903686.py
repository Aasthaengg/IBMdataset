
S = input()

lis = [1,0,0,0]
nlis = [1,0,0,0]

for s in S:

    if s == "?":

        nlis[0] += lis[0] * 2
        nlis[1] += lis[1] * 2
        nlis[2] += lis[2] * 2
        nlis[3] += lis[3] * 2

    if s == "A" or s == "?":

        nlis[1] += lis[0]

    if s == "B" or s == "?":

        nlis[2] += lis[1]

    if s == "C" or s == "?":

        nlis[3] += lis[2]

    lis = []
    for i in range(4):

        lis.append(nlis[i] % (10 ** 9 + 7))

print (lis[3]  % (10 ** 9 + 7))
