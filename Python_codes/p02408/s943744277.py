# coding: utf-8
# Here your code !

n = input()

A = []
for i in range(n):
    A.append(raw_input().split())
    
s = []
h = []
c = []
d = []  # mark???????????????
for i in range(n):
    if A[i][0] == 'S' :
        s.append(int(A[i][1]))
    elif A[i][0] == 'H':
        h.append(int(A[i][1]))
    elif A[i][0] == 'C':
        c.append(int(A[i][1]))
    elif A[i][0] == 'D':
        d.append(int(A[i][1]))

for i in range(1,14): #1-13?????§?????????
    judge = True
    for j in range(len(s)): 
        if i == s[j] :
            judge = False
            break
    if judge :    
        print "S",i
for i in range(1,14): #1-13?????§?????????
    judge = True
    for j in range(len(h)): 
        if i == h[j] :
            judge = False
            break
    if judge :    
        print "H",i
for i in range(1,14): #1-13?????§?????????
    judge = True
    for j in range(len(c)): 
        if i == c[j] :
            judge = False
            break
    if judge :    
        print "C",i
for i in range(1,14): #1-13?????§?????????
    judge = True
    for j in range(len(d)): 
        if i == d[j] :
            judge = False
            break
    if judge :    
        print "D",i