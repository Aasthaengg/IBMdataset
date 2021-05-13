# 解説

n,m = map(int, input().strip().split(' '))
x = list(map(int, input().strip().split(' ')))
y = list(map(int, input().strip().split(' ')))

X = sum([(2*i-n+1)*x[i] for i in range(n)]) % 1000000007
Y = sum([(2*i-m+1)*y[i] for i in range(m)]) % 1000000007
ans = (X*Y) % 1000000007
print(ans)
