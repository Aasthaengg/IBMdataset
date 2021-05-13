n,i = map(int,input().split())
x = []
for t in range(n+1):
    x.append(t)
print(x[n-i+1])