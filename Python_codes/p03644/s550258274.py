def lo2(n):
    count=0
    while n%2==0:
        count+=1
        n=n//2
    return count

N = int(input())

ans = 1
ma = 0
for i in range(1,N+1):
    if lo2(i)>ma:
        ans = i
        ma=lo2(i)

print(ans)
