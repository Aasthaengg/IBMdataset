
f = [-1 for i in range(45)]
f[0] = f[1] = 1

def fib(n):
    global f
    for i in range(2,n+1):
        f[i] = f[i - 1] + f[i - 2]
        #print(i,f[i])
    return f[n]

if __name__ == "__main__":
    n = input()
    n = int(n)
    #print(type(n))
    print(fib(n))

