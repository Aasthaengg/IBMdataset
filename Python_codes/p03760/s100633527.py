O=input()
E=input()

N=len(O)
M=len(E)
ans=""
for i in range(N):
    ans+=O[i]
    if N-M==1 and i==M:
        break
    ans+=E[i]
print(ans)