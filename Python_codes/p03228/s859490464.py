def cookie_T(a,b):
    if a%2!=0:
        a-=1
    b+=(a//2)
    a=a//2
    return a,b
def cookie_A(a,b):
    if b%2!=0:
        b-=1
    a+=(b//2)
    b=b//2
    return a,b
A,B,K=map(int,input().split())
for i in range(K):
    if i%2==0:
        A,B=cookie_T(A,B)
    else:
        A,B=cookie_A(A,B)
print("{} {}".format(A,B))