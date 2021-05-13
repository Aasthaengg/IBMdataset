n=int(input())
s1=input()
s2=input()

mod=1000000007

x=0
cnt=1
while x<n:
    if x==0:
        if s1[x]==s2[x]:
            cnt*=3%mod
            x+=1
        else:
            cnt*=6%mod
            x+=2
    else:
        if s1[x-1]==s2[x-1]:
            #x-1:AA 
            #x  :BB CC
            if s1[x]==s2[x]:
                cnt*=2%mod
                x+=1
            #x-1:AA 
            #x  :BC  CB
            #    BC  CB
            else:
                cnt*=2%mod
                x+=2
        else:
            #x-1:AB
            #   :CC
            if s1[x]==s2[x]:
                cnt*=1%mod
                x+=1
            #x-1:AB
            #x  :BA CA BC 
            else:
                cnt*=3%mod
                x+=2

print(cnt%mod)




