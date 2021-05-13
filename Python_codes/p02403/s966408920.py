# coding: utf-8

while True:
    a,b = map(int, input().split())
    
    if a == b == 0:
        break
    
    for i in range(a):
        for j in range(b):
            print("#",end="")
        print()
        
    print()