N=int(input())
ans=N-1 if 3<N else 0
for a in range(2,int(N**0.5)+1):
    if N%a== 0 and N//a != a:
        b = N//a-1
        if N%b==N//b:
            ans+=b
print(ans)