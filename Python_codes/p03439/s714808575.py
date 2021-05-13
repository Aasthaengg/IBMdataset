n=int(input())
def ceil(a,b):
    ret = -(-a//b)
    if ret%2==0:
        return ret
    else:
        return ret+1

print(0)
first=input()
if first=="Vacant":
    exit()

l=0
r=n

while abs(l-r)>5:
    nxt = ceil(l+r,2)
    print(nxt)
    ans=input()
    if ans=="Vacant":
        exit()
    if ans==first:
        l=nxt
    else:
        r=nxt


for i in range(l,r):
    print(i)
    ans=input()
    if ans=="Vacant":
        exit()