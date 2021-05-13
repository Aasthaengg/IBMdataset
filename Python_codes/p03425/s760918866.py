n=int(input())
M=A=R=C=H=0
for i in range(n):
    s=input()
    if s[0]=="M":   M+=1
    elif s[0]=="A": A+=1
    elif s[0]=="R": R+=1
    elif s[0]=="C": C+=1
    elif s[0]=="H": H+=1
a=[M,A,R,C,H]
from itertools import combinations
ans=0
for L in list(combinations(a,3)):
    ans+=L[0]*L[1]*L[2]
print(ans)