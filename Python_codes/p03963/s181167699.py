N = list(map(int,input().split()))
ans = N[1]
for i in range(N[0]-1):
    ans *= N[1]-1
print(ans)