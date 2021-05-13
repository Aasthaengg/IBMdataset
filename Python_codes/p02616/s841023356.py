n,k=map(int,input().split())
a=list(map(int,input().split()))

mainasu=[]
purasu=[]
for aa in a:
    if aa>=0:
        purasu.append(aa)
    else:
        mainasu.append(aa*(-1))



mod=10**9+7

#回答がプラスになるケース
if (k<n and len(purasu)>0) or (k<n and k%2==0) or (k==n and len(mainasu)%2==0):
    p_pos=0
    m_pos=0
    mainasu.sort(reverse=True)
    purasu.sort(reverse=True)
    ans=1
    cnt=0
    while cnt<k:
        ans=ans%mod
        #どっちからでも選べる
        if p_pos<len(purasu) and m_pos+1 < len(mainasu) and cnt<k-1:
            #もし最後から2つ目
            if cnt<=k-2:
                if p_pos==len(purasu)-1:
                    ans*=mainasu[m_pos]%mod
                    m_pos+=1
                    ans*=mainasu[m_pos]%mod
                    m_pos+=1
                    cnt+=2
                elif purasu[p_pos]*purasu[p_pos+1]>mainasu[m_pos]*mainasu[m_pos+1]:
                    if cnt==k-2:
                        ans*=purasu[p_pos]%mod
                        p_pos+=1
                        ans*=purasu[p_pos]%mod
                        p_pos+=1
                        cnt+=2
                    else:
                        ans*=purasu[p_pos]%mod
                        p_pos+=1
                        cnt+=1

                else:
                    ans*=mainasu[m_pos]%mod
                    m_pos+=1
                    ans*=mainasu[m_pos]%mod
                    m_pos+=1
                    cnt+=2
            else:
                if purasu[p_pos]>mainasu[m_pos+1]:
                    ans=ans*purasu[p_pos]%mod
                    cnt+=1
                    p_pos+=1
                else:
                    ans*=mainasu[m_pos]%mod
                    m_pos+=1
                    ans*=mainasu[m_pos]%mod
                    m_pos+=1
                    cnt+=2
        elif p_pos<len(purasu):
            ans=ans*purasu[p_pos]%mod
            cnt+=1
            p_pos+=1
        else:
            ans*=mainasu[m_pos]%mod
            m_pos+=1
            ans*=mainasu[m_pos]%mod
            m_pos+=1
            cnt+=2
    print(ans%mod)









#回答がマイナスになるケース
else:
    pm=purasu+mainasu
    pm.sort()
    ans=1
    for i in range(k):
        ans=ans*pm[i]%mod
        ans=ans%mod
    #print(-1*ans)
    print((-1*ans)%mod)






