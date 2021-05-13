S=input()
N=len(S)
D={"a":0,"b":0,"c":0}
for i in range(N):
    D[S[i]]+=1

if N==1:
    print("YES")
    exit()
elif N==2:
    if len(set(S))==1:
        print("NO")
    else:
        print("YES")
    exit()


a=D["a"]
b=D["b"]
c=D["c"]
MIN=min(a,b,c)
MAX=max(a,b,c)

if MAX-MIN<=1:
    print("YES")
else:
    print("NO")