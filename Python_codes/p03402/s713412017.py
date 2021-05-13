a,b=map(int,input().split())
print(100,100)
for i in range(50):
    for j in range(100):
        if a-1and i%2and j%2:
            print('.',end='')
            a-=1
        else:
            print('#',end='')
    print()
for i in range(50):
    for j in range(100):
        if b-1and i%2and j%2:
            print('#',end='')
            b-=1
        else:
            print('.',end='')
    print()