A,B,C,D = map(int,input().split())

if abs(A-B) <= D and abs(B-C) <= D or abs(A-C)<= D:
    print('Yes')
else:
    print('No')