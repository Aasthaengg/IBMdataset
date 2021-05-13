T=input()

N=len(T)
ans=""
for i in range(N):
    if T[i]=="?":
        ans+="D"
    else:
        ans+=T[i]
print(ans)