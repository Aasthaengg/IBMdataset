n=int(input())
a=[int(input()) for i in range(n)]
A,B=sorted(a,reverse=True)[0:2]
for i in range(n):
    if a[i]==A:
        print(B)
    else:
        print(A)