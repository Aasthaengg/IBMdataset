S=input()

R=0
B=0
for s in S:
    if s=="0":
        R+=1
    else:
        B+=1

print(2*min(R,B))
