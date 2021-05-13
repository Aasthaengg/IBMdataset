import sys

N = int(input())
D = sorted(list(map(int,input().split())))

if N % 2 != 0:
    print(0)
    sys.exit()

low  = D[0:N//2]
high = D[N//2::]

flg  = all( low[-1] + 1 >  x for x in low )
flg |= all( high[0] - 1 >= x for x in high )

if flg == True:
    print(high[0] - low[-1])
else:
    print(0)

