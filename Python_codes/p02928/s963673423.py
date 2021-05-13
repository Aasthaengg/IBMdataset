n, k = map(int, input().split())
A = list(map(int, input().split()))
mod = pow(10,9)+7
ans_p1 = 0
for i in range(n):
    ans_p1 += sum([bool(A[i]>A[j]) for j in range(i+1,n)])

ans_p2 = 0
for i in range(n):
    ans_p2 += sum([bool(A[i]>A[j]) for j in range(n)])
print((ans_p1*k+ans_p2*k*(k-1)//2)%mod)