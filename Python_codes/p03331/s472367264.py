def main():
    n = int(input())

    minSum = 10**18

    for a in range(1, n):
        b = n - a

        sumA = 0
        sumB = 0

        for digit in str(a):
            sumA += int(digit)
        
        for digit in str(b):
            sumB += int(digit)
        
        total = sumA + sumB
        
        if total < minSum:
            minSum = total
    
    print(minSum)

if __name__ == '__main__':
    main()