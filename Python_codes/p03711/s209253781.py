A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
C = [2]
x,y = map(int,input().split())
if x==y==2 or x in A and y in A or x in B and y in B:
    print('Yes')
else:
    print('No')