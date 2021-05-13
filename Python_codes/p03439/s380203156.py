import sys
n=int(input())

l=0
print(l)
sys.stdout.flush()
sl=input()
if sl=="Vacant":
    exit()
r=n-1
print(r)
sys.stdout.flush()
sr=input()
if sr=="Vacant":
    exit()



for _ in range(18):
    m=(l+r)//2
    print(m)
    sys.stdout.flush()
    s=input()
    if s=="Vacant":
        exit()
    if (m-1-l)%2 and s!=sl:
        sr=s
        r=m
    if (m-1-l)%2==0 and s==sl:
        sr=s
        r=m
    if (r-m-1)%2 and s!=sr:
        sl=s
        l=m
    if (r-m-1)%2==0 and s==sr:
        sl=s
        l=m
