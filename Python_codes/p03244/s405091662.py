n=int(input())
V=list(map(int,input().split()))

from collections import Counter
V_1=V[::2]
V_2=V[1::2]

V_1_counter=Counter(V_1).most_common()
V_2_counter=Counter(V_2).most_common()
c1 = V_1_counter
c2 = V_2_counter

if c1[0][0]!=c2[0][0]:
    print(n-c1[0][1]-c2[0][1])
if c1[0][0]==c2[0][0]:
    if len(c1)==len(c2)==1:
        print(n//2)
    if len(c1)==1 and len(c2)!=1:
        print(n-c1[0][1]-c2[1][1])
    if len(c2)==1 and len(c1)!=1:
        print(n-c1[1][1]-c2[0][1])    
    if len(c1)>1 and len(c2)>1:    
        print(n-max(c1[1][1]+c2[0][1],c1[0][1]+c2[1][1]))