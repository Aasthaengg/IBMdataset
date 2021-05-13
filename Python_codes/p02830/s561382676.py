N = int(input())
S,T=input().split()
lists=[]
for i in range(N):
    lists+=S[i]
    lists+=T[i]
print(*lists,sep="")
   

    
