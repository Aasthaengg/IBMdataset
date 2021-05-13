n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
sum_a = 0
for i in range(n):
    sum_a += A[i]
    temp = sum_a
    for j in range(i,n):
        temp += B[j]
    ans = max(ans,temp)

print(ans)