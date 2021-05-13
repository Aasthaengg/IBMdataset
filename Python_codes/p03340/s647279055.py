N=int(input())
A=list(map(int,input().split()))
l=0 #[l r)
r=1
buf=0
cnt=0
ans=[]
su=0
i=0
length=0
while r<=N:
    if buf+A[r-1]==buf^A[r-1]:
        length=length+1
        buf=buf^A[r-1]
        r=r+1
    else:
        buf=buf^A[l]
        l=l+1
        cnt=0
        su=su+length
        length=length-1
        if r==l:
            r=r+1
    #print(buf,cnt,su)
    #input()
#print(l,r)
#su=su+cnt
#for i in range(len(ans)):
#    cnt=cnt+(ans[i]*(ans[i]+1))//2
print(su+((r-l-1)*(r-l))//2)
#1+2+1+1