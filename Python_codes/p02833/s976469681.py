N = int(input())

k = 5
ans = 0
if N%2>0:
    print(0)
    exit()
while k<N:
    ans += (N//2)//k
    k*=5
print(ans)


