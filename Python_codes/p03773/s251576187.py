A,B = map(int,input().split())
N = A + B
if N <24:
    print(N)
elif N >= 24:
    print(N-24)