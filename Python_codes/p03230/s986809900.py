import sys


N = int(input())


k = 0

while k*(k+1) <= 2 * N:

    if k * (k+1) == 2 * N:

        lis = [ [] for i in range(k+1) ]
        now = 1

        for i in range(k):

            for j in range(k-i):

                lis[i].append(now)
                lis[i+1+j].append(now)
                now += 1
        print ("Yes")
        print (k+1)
        for i in range(k+1):
            print (k," ".join(map(str,lis[i])))
        sys.exit()

    k += 1

print ("No")