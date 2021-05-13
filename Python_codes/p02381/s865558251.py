import math

while 1 :
    n = int( input().strip() )
    if n == 0 :
        break

    s = input().strip().split()
    for i in range(0, len(s)) :
        s[i] = float(s[i])

    m = sum(s)/n

    sigma = sum( [ ( si - m ) ** 2 for si in s ] )

    a = math.sqrt( sigma/n )
    print("{0:.8f}".format(a))
