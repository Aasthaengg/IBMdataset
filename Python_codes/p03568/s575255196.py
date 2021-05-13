N=int(input())
A=list(map(int, input().split()))

ans=3**N
sub=1
for a in A:
    if a%2==0:
        sub*=2
    else:
        continue
ans-=sub
print(ans)