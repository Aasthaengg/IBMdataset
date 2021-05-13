# coding: utf-8
# Here your code !
while True:
    a,b = map(int, input().split())
    
    if a == b == 0:
        break
    
    for i in range(a):
        for j in range(b):
            if (i + j) % 2 == 0:
                print("#",end="")
            else:
                print(".",end="")
        print()
        
    print()