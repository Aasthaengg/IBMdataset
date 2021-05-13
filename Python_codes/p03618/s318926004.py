from collections import Counter


A=list(input())
N=len(A)

num=Counter(A)

S=N*(N-1)//2+1

for i in num.values():
    if i==1:continue
    else:
        S=S-i*(i-1)//2

print(S)