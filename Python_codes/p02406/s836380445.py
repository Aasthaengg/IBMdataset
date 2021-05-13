def call(n):
    print "",
    i = 1
    while i <= n:
        x = i
        if x % 3 == 0:
            print str(i),
            i += 1
            continue

        while x:
            if x % 10 == 3:
                print str(i),
                break
            x /= 10
            
        i += 1
        
    print

n = int(raw_input())
call(n)