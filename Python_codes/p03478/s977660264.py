def SumReturn(num):
    total=0
    while num!=0:
        total += num%10
        num //= 10
        
    return total

if __name__ == '__main__':
    
    n, a, b = map(int, input().split())
    
    sum = 0
    
    for i in range(1, n+1):
        
        if SumReturn(i)>=a and SumReturn(i)<=b:
            sum += i
            
    print(sum)