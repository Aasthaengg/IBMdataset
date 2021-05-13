H = int(input())
W = int(input())
N = int(input())

m = max(H, W)
n = 0
while True:
    n += 1
    if n*m >= N:
        print(n)
        break