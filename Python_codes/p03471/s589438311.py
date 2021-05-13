s=list(map(int,input().split()))
ans=[]
a=int(s[1]/10000)
b=int(s[1]/5000)
c=int(s[1]/1000)
for i in range(0,a+1):
    for j in range(0,b+1):
        if(s[0]-i-j>=0):        
            check=10000*i+5000*j+1000*(s[0]-i-j)
            if(check==s[1]):
                ans.append(i)
                ans.append(j)
                ans.append(s[0]-i-j)
                break
                
if(ans==[]):
    print('-1 -1 -1')
else:
    print('{} {} {}'.format(ans[0],ans[1],ans[2]))          