n = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(n):
    k = A[i]
    while ~k&1:
        k //= 2
        ans +=1
print(ans)