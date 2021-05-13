n= int(input())
s1=input()
s2=input()
index=0
s=''
while index<n:
    if s1[index]==s2[index]:
        index+=1
        s=s+'t'
    else:
        index+=2
        s=s+'y'
adict = {'tt':2,'ty':2,'yt':1,'yy':3}
ans = 0
if s[0]=='t':ans=3
else:ans=6
for i in range(len(s)-1):
    ans = (ans%1000000007) * (adict[s[i:i+2]]%1000000007) % 1000000007
print(ans)