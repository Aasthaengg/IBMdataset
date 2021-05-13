n = int(input())

def call(n):
    i = 0
    while True:
        i += 1
        if i > n:
            break
        x = i
        if x % 3 == 0:
            print(' ' + str(i), end = '')
            continue

        while True:
            if int(x) % 10 == 3:
                print(' ' + str(i), end = '')
                break
            x /= 10
            if x == 0:
                break
            
    print()
    
call(n)