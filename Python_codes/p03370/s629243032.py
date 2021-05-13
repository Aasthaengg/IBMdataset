n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
l = []
for i in range(n):
    X = (x - sum(m)) // m[i]
    l.append(X)
    
print(n + max(l))