X,A,B=list(map(int, input().split()))
if A>=B:
    print('delicious')
elif X+A>=B:
    print('safe')
else:
    print('dangerous')