#1_10_A
n = int(input())
MEMO = [None] * (n + 1)

def Fib(i):
    if i == 0 or i == 1:
        return 1
        
    if MEMO[i]:
        return MEMO[i]
    
    r =  Fib(i-1) + Fib(i-2)
    MEMO[i] = r
    return r
     
print(Fib(n))
