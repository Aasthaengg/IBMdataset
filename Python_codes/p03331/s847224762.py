
N = int(input())

if N in [10**i for i in range(1, 6)] :
    print("10")
else :
    print(sum(map(int, str(N))))
