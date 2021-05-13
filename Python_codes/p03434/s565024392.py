import math
N=int(input())
a=list(map(int,input().split()))
a=sorted(a)
alice=0
bob=0
if(N%2==0):
    for i in range(0,N-1,2):
        alice=a[i+1]+alice
        bob=a[i]+bob
else:
    for i in range(1,N-1,2):
        alice=a[i+1]+alice
        bob=a[i]+bob
    alice=alice+a[0]
print(alice-bob)