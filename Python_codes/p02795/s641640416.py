h=int(input())
w=int(input())
n=int(input())

cnt=0
ans=0
while cnt<n:

    if h>=w:
        cnt+=h

    elif h<w:
        cnt+=w
    ans+=1

print(ans)