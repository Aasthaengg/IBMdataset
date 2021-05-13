n = int(input())

l = [1,1]

if n in [0,1]:
    print(1)
else:
    for i in range(2, n+1):
        fib = l[-1] + l[-2]
        l.append(fib)
    print(fib)


