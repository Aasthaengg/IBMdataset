import sys
N = list(input())

if N.count("9") == len(N):
    print(len(N)*9)
    sys.exit(0)
if N.count("9") == len(N)-1:
    for n in range(len(N)):
        if N[n] != "9":
            if n == 0:
                i = int(N[n])
                print(i+((len(N)-1)*9))
                sys.exit(0)
            else:
                print(8+((len(N)-1)*9))
                sys.exit(0)

for n in range(len(N)-1):
    i = int(N[n])
    if i != 9:
        cnt1 = len(N[:n])
        cnt2 = len(N[n+1:])
        print((cnt1*9)+(i-1)+(cnt2*9))
        sys.exit(0)