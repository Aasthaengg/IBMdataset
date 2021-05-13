import collections

s = input()
K = int(input())

l = len(s)
sub = set()

if l <= 50:
    for i in range(l):
        for j in range(i+1):
            sub.add(s[j:i+1])
    #print(sub)
    subl = list(sub)
    subl.sort()
    #print(subl)
    print(subl[K-1])

else:
    cl = collections.Counter(s).most_common()
    cl.sort(key=lambda x: x[0])
    #print(cl)
    d = 0
    while len(sub) < K:
        be = cl[d][0]
        for i in range(l):
            if s[i] == be:
                for j in range(K):
                    sub.add(s[i:min(i+j+1,l)])
        d += 1
    #print(sub)
    subl = list(sub)
    subl.sort()
    print(subl[K-1])
