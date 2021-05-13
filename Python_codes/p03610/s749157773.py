S=input()
N=len(S)
ans=""

for i in range(N):
    if i%2==0:
        ans+=S[i]
print(ans)