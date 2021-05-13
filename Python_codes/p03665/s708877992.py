N,P = map(int,input().split())
A = list(map(int,input().split()))

if all(a%2==0 for a in A):
    print(0 if P else 2**N)
else:
    print(2**(N-1))