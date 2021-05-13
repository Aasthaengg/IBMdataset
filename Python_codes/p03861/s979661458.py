def main():
    
    end, start, divisor = [int(i) for i in input().split()]
    a = start//divisor - (end-1)//divisor

    print(a)

main()