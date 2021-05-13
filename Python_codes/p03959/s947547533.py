import math
import sys

N = input()
T = [int(i) for i in raw_input().split()]
A = [int(i) for i in raw_input().split()]

ans = 1

if(N==1 and T[0]!=A[0]):
    print '0'
    sys.exit()

for i in range(N):
#    if(i==0 or i==N-1):
#        continue
    
    if(T[i-1]!=T[i] and T[i]>A[i]):
        print '0'
        sys.exit()
    
    if(T[i-1]>T[i]):
        continue

    if(i==N-1):
        continue

    if(A[i+1]!=A[i] and A[i]>T[i]):
        print '0'
        sys.exit()
    
    if(A[i+1]>A[i]):
        continue

    if(i==0):
        continue

    if((T[i-1]!=T[i])or(A[i+1]!=A[i])):
        continue

    else:
        ans *= min(T[i],A[i])
        ans %= 1000000007

    

print ans