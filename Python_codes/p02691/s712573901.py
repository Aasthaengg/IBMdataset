from collections import Counter
n=int(input())
A=list(map(int,input().split()))

B,C=[],[]
for i,j in enumerate(A):
    B.append(i+j+1)
    C.append((i+1)-j)

B,C=Counter(B),Counter(C)
ans=0
for i,j in B.items():
    ans +=j*C[i]
print(ans)