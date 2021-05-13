def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        seq = [0 for _ in range(n+1)]
        seq[0], seq[1] = 1, 1
        for i in range(2,n+1):
            seq[i] = seq[i-1] + seq[i-2]
        return seq[n]

if __name__ == '__main__':
    print(fib(int(input())))
