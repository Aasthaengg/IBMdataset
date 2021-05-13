from collections import Counter
A=list(input())
m=len(A)

B=Counter(A)

cnt=0
for i in A:
    B[i] -=1
    cnt +=B[i]
print(m*(m-1)//2-cnt+1)