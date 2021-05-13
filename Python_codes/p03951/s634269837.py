N=int(input())
S=input()
T=input()

ans=2*N
i=N
while i:
    if S[-i:]==T[:i]:
        ans-=i
        break
    i-=1

print(ans)