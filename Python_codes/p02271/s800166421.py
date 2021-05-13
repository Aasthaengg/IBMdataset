is_able_make = [False]*2000

input()

A = [ int( val ) for val in input().rstrip().split( ' ' ) ]
q = int(input())
M = [ int( val ) for val in input().rstrip().split( ' ' ) ]

for i in A:
    for j in range(2000-i,0,-1):
        if is_able_make[j] == True:
            is_able_make[i+j] = True
    is_able_make[i] = True

for x in M:
    if(is_able_make[x] == True):
        print('yes')
    else:
        print('no')