N=int(input())
print(0,flush=True)
s=input()
if s=="Vacant":
    exit()
cap=0
if s=="Female":
    cap=1
lo=0
hi=N
while(1):
    mid=(lo+hi)//2
    print(mid,flush=True)
    s=input()
    if s=="Vacant":
        exit()
    gen=0
    if s=="Female":
        gen=1
    if (cap+mid)%2==gen:
        lo=mid
    else:
        hi=mid