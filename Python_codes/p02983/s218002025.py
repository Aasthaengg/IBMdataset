L, R = map(int, input().split())
ans = 2019
    
if L//2019 != R//2019:
    print(0)
    exit(0)
else:
    L = L%2019
    R = R%2019

    for i in range(L,R+1):
        for j in range(i+1,R+1):
            ans = min(ans,(i*j)%2019)

print(ans)