N = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
alice = 0
for i in range(0,N,2):
    alice += a[i]
bob = 0
for i in range(1,N,2):
    bob += a[i]
print(alice - bob)