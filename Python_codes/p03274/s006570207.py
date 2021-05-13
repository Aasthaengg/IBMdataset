n,K=(int(i) for i in input().strip().split(" "))
x=[int(i) for i in input().strip().split(" ")]


ans = min(b - a + min(abs(a), abs(b)) for a, b in zip(x, x[K-1:]))
print(ans)