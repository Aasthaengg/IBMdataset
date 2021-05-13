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
            if int(o) == int(w[j])-1:
                print('#')
            elif int(o) == 0:
                print('#',end='')                
            elif int(k) == 0:
                print('#',end='')       
            elif int(k) == int(h[j])-1:
                print('#',end='')     
            else:
                print('.',end='')

    print('')
