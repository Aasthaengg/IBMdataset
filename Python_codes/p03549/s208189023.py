N, M = map(int, input().split())

T = (N-M)*100 + M*1900
a = (1-2**(-M))

ans = 2**(-M)*T//((1-a)**2)

print(int(ans))