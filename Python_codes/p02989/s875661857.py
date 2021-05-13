n = int(input())
D = tuple(map(int, input().split()))
D = sorted(D)

if n%2==1:
    print(0)
else:
    print(D[n//2] - D[n//2-1])