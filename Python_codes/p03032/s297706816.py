n,k=map(int,input().split())
v=list(map(int, input().split()))

if k<n*2:
    ans=0
    for i in range(k+1):
        for j in range(k-i+1):
            v_r=v[:i]
            v_l=v[(n-j):]
            sute_cnt=k-(i+j)
            v_new=v_r+v_l
            v_new.sort()
            # print(i, j, v_r, v_l, sute_cnt, v_new)
            s=sum(v_new)
            if not v_new:
                continue
            for indx in range(len(v_new)):
                if v_new[indx]<0 and sute_cnt>0:
                    s-=v_new[indx]
                    sute_cnt-=1
                else:
                    break
            ans=max(ans,s)
    print(ans)

else:
    ans=0
    for i in range(n):
        if v[i]>=0:
            ans+=v[i]
    print(ans)
