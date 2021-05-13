a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
x,y=map(int,input().split())
print('NYoe s'[(x in a and y in a) or (y in b and y in b)::2] if x!=2 and y!=2 else 'No')