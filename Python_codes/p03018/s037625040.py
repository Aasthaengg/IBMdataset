s=input()
t=''
i=0
while(i<len(s)):
    if i<len(s)-1 and s[i:i+2]=='BC':
        t+='D'
        i+=2
    else:
        t+=s[i]
        i+=1
t=t[::-1]
N=len(t)
i=0
ans=0
while(i<N):
    if t[i]=='D':
        j=i
        cnt=0
        while(j<N and t[j]!='B' and t[j]!='C'):
            if t[j]=='D':
                cnt+=1
            else:
                ans+=cnt
            j+=1
        i=j
    i+=1
print(ans)