S=input()
L=[0,0,0]
for i in range(len(S)):
    if S[i]=="a":
        L[0]+=1
    elif S[i]=="b":
        L[1]+=1
    else:
        L[2]+=1
        
L.sort()
if L[2]-L[0]<=1:
    print("YES")
else:
    print("NO")