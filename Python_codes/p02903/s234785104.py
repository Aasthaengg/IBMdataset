H,W,A,B = map(int,input().split())
X = ''.join(['0']*A+['1']*(W-A))
Y = ''.join(['1']*A+['0']*(W-A))
for i in range(B):
    print(X)
for i in range(H-B):
    print(Y)
