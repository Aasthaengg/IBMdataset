n = int(input())
fib_ls = [0] * (n+1)
fib_ls[0], fib_ls[1] = 1,1
for i in range(2,n+1):
    fib_ls[i] = fib_ls[i-1] + fib_ls[i-2]
print(fib_ls[n])
