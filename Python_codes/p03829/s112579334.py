n,a,b = map(int, input().split())
x = list(map(int, input().split()))
d = [x[i+1]-x[i] for i in range(n-1)]
ans = sum([min(i*a,b)for i in d])
print(ans)