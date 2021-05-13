S=input()
w=int(input())
ans=[]
count=0

for i in range(len(S)):
    ans+=S[count]
    count+=w
    if count>=len(S):
        break
    
ansans=''.join(ans)
print(ansans)