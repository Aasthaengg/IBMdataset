N,A,B = map(int, input().split())
balls = A+B
an = 0
if N % balls == 0:
    print(int(A * (N//balls)))
else:
    an += A * (N//balls)
    an += min(A,N % balls)
    print(an)