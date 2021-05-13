N = int(input())
l = list(map(int, input().split()))
a = [0] * (N+1)
for k in reversed(range(1, N+1)):
    num = sum([a[k*i] for i in range(1, N//k+1)])
    if num % 2 != l[k-1]:
        a[k] = 1
M = sum(a)
ans = [i for i in range(1, N+1) if a[i] > 0]
 
print(M)
print(' '.join(map(str, ans)))