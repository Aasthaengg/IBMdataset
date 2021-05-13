n=int(input())
a=[int(i)for i in input().split()]
a.sort()
alice=0
bob=0
for i in range(n):
    if i%2==0:
        alice+=a.pop(-1)
    else:
        bob+=a.pop(-1)
print(alice-bob)