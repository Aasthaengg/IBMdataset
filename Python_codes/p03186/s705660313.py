a,b,c=map(int,open(0).read().split())
count=0
count+=min(b,c)*2
b-=count//2
c-=count//2
if b==0:
    if a<c:
        count+=a+1
    else:
        count+=c
else:
    count+=b
print(count)