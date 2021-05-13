n,p = map(int, input().split())
a = list(map(int,input().split()))
if all(i%2==0 for i in a):
    print(0 if p==1 else 2**n)
else:
    print(2**(n-1))
