A, B, K = list(map(int, input().split()))

ans=0
res=0
for i in range(min(A, B), 0, -1):
    if A%i==0 and B%i==0:
        res+=1
        if res==K:
            ans=i
            break

print(ans)