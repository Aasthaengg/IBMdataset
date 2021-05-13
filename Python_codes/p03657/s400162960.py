#!/usr/bin/env python3
a,b = map(int,input().split())
if (a % 3)*(b % 3) % 3 != 1:
    print("Possible")
else:
    print("Impossible")