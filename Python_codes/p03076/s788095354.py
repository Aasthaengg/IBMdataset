S = [int(input()) for _ in range(5)]
l=[]
m=10
for i in range(5):
    if (S[i]%10)<m and S[i]%10!=0:
        m=S[i]%10
        a=S[i]
        j=i
if m==10:
    a=S[0]  
    j=0      
for i in range(5):
    if  i!=j:
        if S[i]%10!=0:
            S[i]+=10-(S[i]%10)
        l.append(S[i])
l.append(a)
print(sum(l))