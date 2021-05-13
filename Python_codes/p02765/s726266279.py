N,R = list(map(int, input().split()))

if N<10:
    R = R + 100*(10-N)

print(R)