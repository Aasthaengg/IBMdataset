N,X= map(int,input().split())
A = [int(a) for a in input().split()]
A.sort()

tmp = 0
ans = 0

for a in A:
    tmp+=a
    if tmp<=X:
        ans+=1
if ans==N and tmp<X:
    ans-=1
print(ans)