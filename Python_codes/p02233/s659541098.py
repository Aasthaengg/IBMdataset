def main():
    def fib(n):
        a = 1
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(n-1):
                a, b = b, a + b
            return b
    
    n = int(input())
    print(fib(n))
        
if __name__ == '__main__':
    main()
