while True:
    a,b= map(int,input().split())
    if(a==0 and b==0):
        break;
    for i in range(a):
        for j in range(b):
            if( i == 0 or i == a-1):
                print('#',end='') 
            elif(j == 0):
                    print('#',end='')
            elif(j > 0 and j < b-1):
                    print('.',end='')
            elif(j==b-1):
                    print('#',end='')
        print()
    print()
               
