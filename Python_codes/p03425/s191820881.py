N=int(input())
lst=[]
s1=0
s2=0
s3=0
s4=0
s5=0
for i in range(N):
    s=input()
    if s[0]=="M":
        s1+=1
    elif s[0]=='A':
        s2+=1
    elif s[0]=="R":
        s3+=1
    elif s[0]=="C":
        s4+=1
    elif s[0]=="H":
        s5+=1
ans=0
ans+=s1*s2*s3
ans+=s1*s2*s4
ans+=s1*s2*s5
ans+=s1*s4*s5
ans+=s1*s3*s5
ans+=s1*s3*s4
ans+=s2*s3*s4
ans+=s2*s3*s5
ans+=s3*s4*s5
ans+=s2*s4*s5
print(ans)
