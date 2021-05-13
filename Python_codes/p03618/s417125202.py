S=list(input())
A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

L=[0 for i in range(26)]

for i in range(len(S)):
    for j in range(26):
        if S[i]==A[j]:
            L[j]+=1
            
#print(L)
ans=1
num=sum(L)
for i in range(26):
    ans+=L[i]*(num-L[i])
    num-=L[i]
print(ans)