a = input()
i = 0
v = 0
for i in range(int(a)):
    if ((int(i)+1) % 3) == 0:
        print(' {}'.format(int(i)+1),end='')
    elif((int(i)+1) % 10) == 3:
        print(' {}'.format(int(i)+1),end='')
    else:
        x = int(i) + 1
        while v == 0:
            
            x = int(x) // 10
            if (int(x) > 10) and (not(int(x) % 10) == 3):
                pass
            elif (int(x) % 10) == 3:
                print(' {}'.format(int(i)+1),end='')
                v = 1
            else:
                v = 1
    v = 0
    
print('')
