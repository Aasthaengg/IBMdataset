n=int(input())
a=list(map(int,input().split()))
a=sorted(a)

alice=0
bob=0
i=0
while a:
    if i%2==0:
        alice+=a.pop()
    else:
        bob+=a.pop()
    i+=1
print(alice-bob)