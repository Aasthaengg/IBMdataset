def call(n):
    s = ''
    for i in range(1,n+1):
        x = i
        if x%3 == 0:
            s += ' '+str(i)
            continue
        while x > 0:
            if x%10 == 3:
                s += ' '+str(i)
                break
            x //= 10
    print(s)

n = int(input())
call(n)
