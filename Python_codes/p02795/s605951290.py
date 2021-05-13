H = int(input())
W = int(input())
N = int(input())

a = max(H,W)

if N%a == 0:
    print(N//a)
else:
    print(N//a+1)
