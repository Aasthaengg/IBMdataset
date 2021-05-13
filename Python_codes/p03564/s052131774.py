n = int(input())
k = int(input())

for i in range(5):
    a = 2**i
    if a >= k:
        b = i
        break

res = 1

res = res*(2**(min(n,b))) + k*max(0,(n-b))
print(res)