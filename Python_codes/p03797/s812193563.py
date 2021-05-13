N,M=map(int,input().split())

def check(i):
    if M<i*2:
        return False
    if N+(M-i*2)//2<i:
        return False
    return True

r=M//2+1
l=0
while r-l>1:
    mid=(r+l)//2
    #print(mid,check(mid))
    if check(mid):
        l=mid
    else:
        r=mid
print(l)