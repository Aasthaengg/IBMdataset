s=input()
n=len(s)

count0=0
for i in range(n):
    if s[i]=='0':
        count0+=1

count1=n-count0

if count0<=count1:
    ans=count0*2
else:
    ans=count1*2

print(ans)