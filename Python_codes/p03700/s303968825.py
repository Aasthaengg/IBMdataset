n,a,b=map(int,input().split())
h=[int(input()) for _ in range(n)]

#二部探索

ll=0
rr=10**9+1
ab=a-b
while ll<rr:
    half=(ll+rr)//2

    cnt=0
    for hh in h:
        if hh>b*half:
            cnt+=(-1*((-1*(hh-b*half))//ab))
    
    if cnt>half:
        ll=half+1
    elif cnt<half:
        rr=half
    else:
        print(half)
        exit()
print(ll)


    
