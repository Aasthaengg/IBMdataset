def SumReturn(num):
    total=0
    while num!=0:
        total += num%10
        num //= 10
        
    return total

if __name__ == '__main__':
    
    n = int(input())
    min = 10000
    
    for i in range(1,n):
        if(min > SumReturn(i)+SumReturn(n-i)):
            min = SumReturn(i)+SumReturn(n-i)
        
        
    print(min)