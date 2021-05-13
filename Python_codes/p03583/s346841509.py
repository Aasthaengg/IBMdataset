N = int(input())
import sys

for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n - N*n - N*h > 0:
            if (N*h*n / (4*h*n - N*n - N*h)) == (N*h*n // (4*h*n - N*n - N*h)):
                print(h,n,N*h*n // (4*h*n - N*n - N*h))
                sys.exit()