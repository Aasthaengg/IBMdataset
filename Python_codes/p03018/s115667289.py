s=input() 
n=len(s)
cnt=0
temp=[0]*n
JinA=[] 
for i in range(n-1):
    if s[i]=="A":
        if i>0:
            temp[i]+=temp[i-1]+1 
        else:
            temp[i]+=1
    if s[i]=="B" and s[i+1]=="C" and i>0:
        temp[i+1]+=temp[i-1]
        cnt+=temp[i-1] 

print(cnt)