import sys
N = int(input())
An = list(map(int,input().split()))
a = 1
if 0 in An:
    print("0")
    sys.exit()
else:
    for i in range(N):
        a *= An[i]
        if a > 10**18:
            print("-1")
            sys.exit()
    if a <= 10**18:
        print(a)
        sys.exit()
