N,K=map(int, input().split())

x=N%K

if x ==0:
    print(0)
elif abs(x - K) > x:
    print(x)
else:
    print(abs(x - K))