N,A,B = (int(x) for x in input().split())
if N == 1:
    if A != B:
        print('0')
    else:
        print('1')
elif A > B:
    print('0')
elif A == B:
    print('1')
else:
    print((N-2)*(B-A)+1)