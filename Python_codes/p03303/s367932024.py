S=input()
N=int(input())
ans=""
k=0
for i in S:
        if k%N==0:
                ans+=i
        k+=1
print(ans)