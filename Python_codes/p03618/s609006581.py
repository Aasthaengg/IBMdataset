from collections import Counter
A=input()

N=len(A)
C=Counter(A)
ans=N*(N-1)//2
for v in C.values():
    ans-=(v*(v-1)//2)

print(1+ans)