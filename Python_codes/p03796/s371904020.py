n = int(input())
mod = 10 ** 9 + 7
res = 1
for i in range(2, n+1):
    res = res * i % mod    
print(res)