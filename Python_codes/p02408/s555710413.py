S =[i+1 for i in xrange(13)]
H =[i+1 for i in xrange(13)]
C =[i+1 for i in xrange(13)]
D =[i+1 for i in xrange(13)]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

n = input()
for i in xrange(n):
    c, a = raw_input().split()
    if c == "S":
        for j in xrange(len(S)): 
            if S[j-1] == int(a):
             del S[j-1]
    elif c == "H":
        for j in xrange(len(H)): 
            if H[j-1] == int(a):
             del H[j-1]      
    elif c == "C":
        for j in xrange(len(C)): 
            if C[j-1] == int(a):
             del C[j-1]      
    elif c == "D":
        for j in xrange(len(D)): 
            if D[j-1] == int(a):
             del D[j-1]

for i in xrange(len(S)):
    print "S " + str(S[i])
    
for i in xrange(len(H)):
    print "H " + str(H[i])    
    
for i in xrange(len(C)):
    print "C " + str(C[i])    
    
for i in xrange(len(D)):
    print "D " + str(D[i])   