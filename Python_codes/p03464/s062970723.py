import sys

def updiv(a,b):

    if a % b == 0:
        return a // b
    else:
        return a // b + 1

K = int(input())

A = list(map(int,input().split()))
A.reverse()

mini = 2
maxi = 2

for i in range(K):

    mini = updiv(mini, A[i]) * A[i]
    maxi = maxi // A[i] * A[i]

    if mini > maxi:
        print (-1)
        sys.exit()

    maxi += A[i]-1

print (mini,maxi)
