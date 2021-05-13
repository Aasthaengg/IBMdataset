import math
import sys
N,Y= map(int, input().split()) 
for a in range(N+1):
    for b in range(N+1-a):
        if (10000*a+5000*b+1000*(N-a-b)==Y):
            print(a, b, N-a-b)
            sys.exit()
print(-1, -1, -1)