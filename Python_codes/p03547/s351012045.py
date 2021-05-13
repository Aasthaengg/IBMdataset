h=list('ABCDEF')
X,Y=input().split()
if X==Y: print('=')
else: print('<' if h.index(X)<h.index(Y) else '>')