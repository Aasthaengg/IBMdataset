from collections import deque

def getInts():
    return [ int(x) for x in input().split() ]

def f(A,B):
    return A**5 - B**5

[X] = getInts()
Q = deque([(0,0)])
V = set()
A, B = 0,0
r = []
while not r:
    (A,B) = Q.pop()
    l = [(A+1,B),(A,B+1),(A+1,B+1)]
    l = filter(lambda x: x not in V, l)
    for each in l:
        V.add(each)
        Q.appendleft(each)
    
    r = list(filter(lambda x: f(*x)==X, [(A,B), (A,-B), (-A,B), (-A, -B)]))

print(r[0][0], r[0][1])