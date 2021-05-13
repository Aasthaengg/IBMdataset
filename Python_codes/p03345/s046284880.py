a,b,c,n = [int(i) for i in input().split()]

if n%2 == 1:
    print(b-a if abs(b-a) < 10**18 else 'Unfair')
else:
    print(a-b if abs(a-b) < 10**18 else 'Unfair')