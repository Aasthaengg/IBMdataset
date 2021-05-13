def ok(n):
    v=n%10
    ret=True
    while n>0:
        ret&=n%10==v
        n//=10
    return ret

N=int(input())
while not(ok(N)):
    N+=1
print(N)