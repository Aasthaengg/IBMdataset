def dig_sum(N):
    ans=0
    while N>0:
        ans+=N%10
        N=N//10
    return ans

N=int(input())
ans=100
for i in range(1,N):
    tmp=dig_sum(i)+dig_sum(N-i)
    if tmp<ans:
        ans=tmp
print(ans)
