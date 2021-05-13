from collections import Counter
import sys
n = int(input())
a = Counter(list(map(int,input().split())))

if n % 2 == 0:
    for k,v in a.items():
        if v != 2:
            print(0)
            sys.exit()

else:
    for k,v in a.items():
        if k == 0:
            if v != 1:
                print(0)
                sys.exit(0)
        else:
            if v != 2:
                print(0)
                sys.exit()
                
print(2**(n//2) % (10**9+7))