n=int(input())

q=0
print(q)
zero=input()

if zero=="Vacant":
    exit()

ll=1
rr=n-1

for _ in range(19):
    q=(ll+rr)//2
    print(q)
    s=input()
    if s=="Vacant":
        exit()
    elif q%2==0:
        if s==zero:
            ll=q+1
        else:
            rr=q
    else:
        if s==zero:
            rr=q
        else:
            ll=q+1

