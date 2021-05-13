a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    s=str(i)
    for j in range(len(s)//2):
        if s[j]!=s[len(s)-j-1]:
            c+=1
            break
            
print(b-a+1-c)