N = int(input())
K = int(input())
a = list(map(int, input().split()))
sum_a = 0

for i in range(N):
    A = 2*a[i]
    B = 2*(K-a[i])
    sum_a += min(A,B)
    
    
print(sum_a)