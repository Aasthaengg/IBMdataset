n = int(input())
A = list(map(int,input().split()))
ok = True
if n%2==1:
    a=sorted(A)
    for i in range(len(a)):
        if i%2==0:
            if a[i]!=i:
                ok = False
        else:
            if a[i]!=i+1:
                ok = False
else:
    a=sorted(A)
    for i in range(len(a)):
        if i%2==1:
            if a[i]!=i:
                ok = False
        else:
            if a[i]!=i+1:
                ok = False
if ok:
    print(2**(n//2)%1000000007)
else:
    print(0)