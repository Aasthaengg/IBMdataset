N = int(input())

ans = 0
for i in range(int(pow(N,1/2))+1):
    if i**2 <=N:
        ans = i**2
print(ans)

