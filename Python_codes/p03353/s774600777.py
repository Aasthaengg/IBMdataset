s=input()
k=int(input())
se=set()
for i in range(len(s)):
    for j in range(1,6):
        if(i+j<=len(s)):
           se.add(s[i:i+j])
    
li=sorted(se)
#print(li)
print(li[k-1])






