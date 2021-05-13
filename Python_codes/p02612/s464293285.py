N = int(input())

while(True) : 
    if N >= 1000 : 
        N -= 1000
    elif N == 0 : 
        print(N)
        exit()
    else : 
        print(1000-N)
        exit()