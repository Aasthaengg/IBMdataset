n = int(input())
f = [1,1]
for i in range(n-1):
    fib = f[-1] + f[-2]
    f.append(fib)
print(f[n])
