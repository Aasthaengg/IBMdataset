N=int(input())
a=list(map(int,input().split()))
l=len(a)
a.sort(reverse=True)
alice=bob=c=0
for i in range(l):
    if c%2==0:
        alice+=a[i]

    else:
        bob+=a[i]
    c+=1
print(alice-bob)

