import sys
 
Tmp = []
Tmp = input().rstrip().split(' ')
A = int(Tmp[0])
B = int(Tmp[1])

#A = 170
#B = 80
print('100 100')

for i in range(50):
    for j in range(100):
        if i==0:
            print('.', end='')
            if  j==99:
                print()
               
            continue
        
        if j==0:
            print('.', end='')
            continue
        elif j==99:
            print('.', end='')
            print()
            continue
        else:
            Tmp1 = i % 2
            Tmp2 = j % 2
            
            if (Tmp1 == 1) and (Tmp2 == 1) and (B > 1):
                print('#', end='')
                B -= 1
            else:
                print('.', end='')
                
for i in range(50):
    for j in range(100):
        if i==0:
            print('#', end='')
            if  j==99:
                print()
            continue
        
        if j==0:
            print('#', end='')
            continue
        elif j==99:
            print('#', end='')
            print()
            continue
        else:
            Tmp1 = i % 2
            Tmp2 = j % 2
            
            if (Tmp1 == 1) and (Tmp2 == 1) and (A > 1):
                print('.', end='')
                A -= 1
            else:
                print('#', end='')
                

