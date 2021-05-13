N = int(input())
Price = 0
Rate  = 380000
for T in range(0,N):
    X,U = input().split()
    if U=='JPY': Price += int(X)
    else: Price += float(X)*Rate
print(Price)