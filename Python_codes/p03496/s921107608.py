n = int(input())
a = list(map(int,input().split()))

if min(a)>=0:
    print(n-1)
    for i in range(1,n):
        print(i,i+1)
elif max(a)<=0:
    print(n-1)
    for i in range(n-1):
        print(n-i,n-i-1)
elif abs(max(a))>abs(min(a)):
    print(2*n-1)
    b = a.index(max(a))
    for i in range(n):
        print(b+1,i+1)
    for i in range(1,n):
        print(i,i+1)
else:
    print(2*n-1)
    b = a.index(min(a))
    for i in range(n):
        print(b+1,i+1)
    for i in range(n-1):
        print(n-i,n-i-1)
