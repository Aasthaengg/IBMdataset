s=int(input())
def collatz(number):            
    if number % 2 == 0:          
        number /= 2              
    else:                        
        number = 3 * number + 1  
    return int(number)
c=0
while s!=1 and s!=2 and s!=4:
    s=collatz(s)
    c=c+1
else:
    print(c+4)