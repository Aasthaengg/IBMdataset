W=raw_input()
T=[]
while 1:
    x=raw_input()
    if x=="END_OF_TEXT": break
    T+=[v.lower() for v in x.split()]
print T.count(W)