N = int(input())
p = 10**9+7
a = pow(10, N, p)
b = pow(9, N, p)
c = pow(8, N, p)
ans = (a-2*b+c)%p
print(ans)