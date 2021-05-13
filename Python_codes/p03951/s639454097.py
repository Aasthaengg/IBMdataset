N=int(input())
a=input()
b=input()
ans=2*N

for i in range(1,N+1):
    if a[N-i:]==b[:i]:
        ans=2*N-i

print(ans)