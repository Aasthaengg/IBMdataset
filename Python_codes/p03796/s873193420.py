N = int(input())
c = 1
for i in range(N):
    c = (c * (i+1) )% (10**9+7)
print(c)