import sys

N,M,K = map(int,input().split())

"""

それぞれA,B回押すとすると
A*(N-B) + B*(M-A) == K

AはM以下
.##
.##
#..
#..

"""

for A in range(M+1):

    for B in range(N+1):

        if A*(N-B) + B*(M-A) == K:
            print ("Yes")
            sys.exit()

print ("No")
