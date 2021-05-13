from itertools import permutations

S=input()
a,b,c="a","b","c"
D={a:0,b:0,c:0}

for s in S:
    D[s]+=1

X=min(D.values())
Y=max(D.values())

if Y-X<=1:
    print("YES")
else:
    print("NO")
