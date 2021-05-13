c=0
i = 0
h = []
w = []
while c == 0:
    a = input().split()
    if int(a[0]) == 0:
        c = 1
    elif int(a[1]) == 0:
        c = 1
    else:
        h.append(a[0])
        w.append(a[1])
        i = int(i) + 1

for j in range(int(i)):
    for k in range(int(h[j])):
        for o in range(int(w[j])):
            if (int(k) % 2) == 0:
                if (int(o) % 2) == 0:
                    if o == int(w[j]) - 1:
                        print('#')
                    else:    
                        print('#',end='')
                else:
                    if o == int(w[j]) - 1:
                        print('.')
                    else:    
                        print('.',end='')
            else:
                if (int(o) % 2) == 0:
                    if o == int(w[j]) - 1:
                        print('.')
                    else:    
                        print('.',end='')
                else:
                    if o == int(w[j]) - 1:
                        print('#')
                    else:    
                        print('#',end='')

    print('')
