X,A,B = map(int,input().split())
if A < B:
    if (B-A) <= X:
        print('safe')
    else:
        print('dangerous')
else:
    print('delicious')