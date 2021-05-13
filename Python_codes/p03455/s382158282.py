a, b = map(int, input().split())  
if 1<=a and b<=10000:             
    if (a*b)%2==0:                
        print('Even')             
    else:                         
        print('Odd')              