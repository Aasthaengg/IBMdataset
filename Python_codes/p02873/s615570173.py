s=input()+"<"; n=len(s)
# print(s,n)
bef=-1 ;ans=0 ;i=0
while i<n:
    
    if s[i]=="<":
        ans+=bef+1
        bef+=1
        i+=1
    else:
        cnt=0
        for j in range(i,n):
            if s[j]==">":
                ans+=cnt
                cnt+=1
            else:
                ans+=cnt
                break
        ans+= max(0, bef+1-cnt)
        bef=0
        i+= cnt +1
print(ans)