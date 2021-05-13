S,T = input().split()
A,B = (int(x) for x in input().split())
U   = input()
if S==U:
    print('{} {}'.format(A-1,B))
else:
    print('{} {}'.format(A,B-1))