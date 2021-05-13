n, m, d = map(int, input().split())
ans = (n-d)*2*(m-1)/n/n
print(ans if d else ans/2)