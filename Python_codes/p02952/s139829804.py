n=input()
len_n=len(n)
i=1
ans=0
while(i<len_n):
    if i%2!=0:
        ans+=9*10**(i-1)
    i+=1
if len_n%2!=0:
    ans+=(int(n)-10**(len_n-1)+1)
print(ans)