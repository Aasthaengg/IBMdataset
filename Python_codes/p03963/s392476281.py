n,k = map(int,input().split())

var = k

for i in range(n-1):
    var *= k-1

print(var)