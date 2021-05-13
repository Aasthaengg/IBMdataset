N, X, T = map(int, input().split())

syo = N // X
amari = N % X

if amari == 0:
    time = syo*T
else: time = (syo+1)*T
print("{}".format(time))