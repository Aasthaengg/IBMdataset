def wa(n):
    return sum(list(map(int,list(str(n)))))

N,A,B = map(int,input().split())

ans = 0
for i in range(1,N+1,1):
    tmp = wa(i)
    if A<=tmp and tmp<=B:
        ans += i

print(ans)
