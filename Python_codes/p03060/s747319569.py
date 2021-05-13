n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
x = [v[i]- c[i] for i in range(n)]
ans = sum(x[i] if x[i] > 0 else 0 for i in range(n))
print(ans)
