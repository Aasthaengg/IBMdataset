import math
N=int(input())
ans=[]
for i in range(1,int(math.sqrt(N))+1):
    if N%i==0:
        num1=i
        num2=N//i
        if (num1-1)>num2:
            ans.append(num1-1)
        if (num2-1)>num1:
            ans.append(num2-1)
#print(ans)
ans=list(set(ans))
print(sum(ans))