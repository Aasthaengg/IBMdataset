s=input()

l=[0]
ans=[0]*(len(s))
for i in range(len(s)-1):
    if s[i]=="L" and s[i+1]=="R":
        l.append(i+1)
       
n=len(l)+1
l.append(len(s))
#print(set(s[l[0]:l[1]]))

for i in range(n-1):
    #print(s[l[i]:l[i+1]])
    for j in range(len(s[l[i]:l[i+1]])-1):
        p=len(s[l[i]:l[i+1]])
        if s[l[i]]=="L":
            ans[l[i]]=p
            break
        if s[l[i+1]-1]=="R":
            ans[l[i+1]-1]=p
            break
        if s[l[i]:l[i+1]][j]=="R" and s[l[i]:l[i+1]][j+1]=="L":
            if j%2==1:
                ans[l[i]+j]=p//2
                ans[l[i]+j+1]=p-p//2
                break
            else:
                ans[l[i]+j]=p-p//2
                ans[l[i]+j+1]=p//2
                break
print(*ans)


            
  
