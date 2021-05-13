A,B,C,K = map(int, input().split())
limit = 1e18

if abs(A-B)>=limit:
    print('Unfair')
else:
    if K%2==0:
        print(A-B)
    else:
        print(B-A)