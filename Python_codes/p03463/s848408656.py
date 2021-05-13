N, A, B = map(int,input().split())
gap = abs(A-B)-1
if gap%2!=0:
    print('Alice')
else:
    print('Borys')
