N = int(input())
A = list(map(int,input().split()))

sum_A = 0
sum_A_even = 0
for n in range(N):
    sum_A += A[n]
    if (n+1) % 2 == 0:
        sum_A_even += A[n]

x1 = sum_A - 2*sum_A_even
ans=[x1]

for n in range(N-1):
#     print(n,ans)
    x_ = ans[n]
    x = 2*A[n] - x_
    ans.append(x)
    
print(' '.join(map(str,ans)))