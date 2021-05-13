a,b=map(int,input().split())
s=[]
for i in range(a,b+1):
    s.append(str(i))
#print(s)
count=0
#print(s[0][0::2])
#print(s[0][-1::-2])
for i in range(len(s)):
    if s[i][0::2]==s[i][-1::-2] and s[i][1::2]==s[i][-2::-2]:
        count+=1
        #print(s[i])
print(count)