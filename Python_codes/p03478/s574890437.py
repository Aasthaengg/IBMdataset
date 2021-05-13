N,A,B = map(int,input().split())

ans = 0
for i in range(1,N+1):
    l = list(str(i))
    new_l = [int(s) for s in l]
    if A <= sum(new_l) <= B:
        ans += i
        
print(ans)