S=input()

i=0
T=[]
while i<len(S):

    if i+1<len(S) and S[i]+S[i+1]=="BC":
        T.append("D")
        i+=2
    else:
        T.append(S[i])
        i+=1
count=0
m=0
Acount=0
#print(T)
for i in range(len(T)):
    if "A"==T[i]:
        Acount+=1
    elif "D"==T[i]:
        count+=Acount
    else:
        Acount=0



#print(T)
print(count)
