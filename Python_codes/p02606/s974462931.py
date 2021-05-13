L,R,D = list(map(int,input().split()))

ans = 0

for i in range(1,R+1):
    if i < L:
        pass
    else:
        if i % D == 0:
            ans += 1
            
print(ans)
