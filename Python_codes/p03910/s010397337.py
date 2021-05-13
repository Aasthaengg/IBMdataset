n=int(input())
i=1
count=0
ans=[]
if n==1:
    print(1)
    exit()

while count<n:
    count+=i
    ans.append(i)
    i+=1
    
#print(ans,count)
if count-n!=0:
    a=ans.pop(count-n-1)
for i in range(len(ans)):
    print(ans[i])