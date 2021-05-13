while True:
    line = list(map(int,input().split()))
    if line==[0,0]: break
    for i in range(line[0]):
        for j in range(line[1]):
            print('#' if (i+j)%2==0 else '.',end='\n' if j==line[1]-1 else '')
    print()