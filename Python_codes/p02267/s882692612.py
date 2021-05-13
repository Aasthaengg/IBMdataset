n=int(input())
S=input().split()
q=int(input())
T=input().split()
cnt=0
B=[]
for i in range(len(T)):
    c=0
    for j in range(len(S)):
        if T[i]==S[j]:
            if c==0:
                cnt+=1
                c+=1  
print(cnt)
