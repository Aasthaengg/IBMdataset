def call(n):
    s = ""
    i = 1
    while i <= n:
        x = i
        if x%3 == 0:
            s += " {0}".format(i)
        else:
            while x > 0:
               if x%10 == 3:
                   s += " {0}".format(i)
                   break
               x = x // 10
        i += 1
    print(s)

m = int(input())
call(m)