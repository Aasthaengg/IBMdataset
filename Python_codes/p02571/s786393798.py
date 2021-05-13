s= input()
t= input()

atmp=2000
for i in range(len(s) - len(t) + 1):
    s1=s[i:i+len(t)]
    #print(s1)
    tmp=0
    for j in range(len(t)):
        if s1[j]!=t[j]:
            tmp+=1
    atmp=min(atmp,tmp)
        
print(atmp)