s=input()
N=len(s)
ans=0
data=[]
i=0
while N>i:
    if s[i]=='A':
        data.append('X')
        i+=1
    elif s[i]=='B' and i<len(s)-1 and s[i+1]=='C':
        data.append('A')
        i+=2
    else:
        index=[]
        count=0
        for j in range(0,len(data)):
            if data[j]=='A':
                index.append(j)
                count+=1

        for j in range(count):
            ans+=index[j]-j
        data=[]
        i+=1
else:
    if data:
        index=[]
        count=0
        for j in range(0,len(data)):
            if data[j]=='A':
                index.append(j)
                count+=1

        s=0
        for j in range(count):
            s+=index[j]-j

        ans+=s

print(ans)