def fib(n, fib_memo=None):                                                                                                                                                    
    if fib_memo == None:                                                                                                                                                      
        fib_memo = [None]*n                                                                                                                                                   
    if n <= 1:                                                                                                                                                                
        return 1                                                                                                                                                              
    else:                                                                                                                                                                     
        if fib_memo[n-1] == None:                                                                                                                                             
            fib_memo[n-1] = fib(n-1, fib_memo)                                                                                                                                
        if fib_memo[n-2] == None:                                                                                                                                             
            fib_memo[n-2] = fib(n-2, fib_memo)                                                                                                                                
        return fib_memo[n-1] + fib_memo[n-2]                                                                                                                                  
                                                                                                                                                                              
                                                                                                                                                                              
if __name__ == '__main__':                                                                                                                                                    
    n = input()                                                                                                                                                               
    print(fib(int(n)))                                                                                                                                                        