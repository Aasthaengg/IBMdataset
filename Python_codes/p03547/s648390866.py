X,Y = input().split()

arb = ['A','B','C','D','E','F']

print('=' if arb.index(X) == arb.index(Y) else '<'  
if arb.index(X) < arb.index(Y) else '>')

