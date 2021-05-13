import sys
fl=sys.stdout.flush
res=['Vacant','Male','Female']

def main():
    n=int(input())
    r=['' for _ in range(n)]
    print(0)
    fl()
    r[0]=input()
    if r[0]==res[0]:
        return
    
    print(n-1) # even
    r[n-1]=input()
    fl()
    if r[n-1]==res[0]:
        return
    ll,rr=0,n-1
    while rr-ll>1:
        mid=(rr+ll)//2
        print(mid)
        fl()
        r[mid]=input()
        if r[mid]==res[0]:
            return
        if (r[mid]==r[rr])^((rr-mid)%2==0):
            ll=mid
        else:
            rr=mid
    
main()
