def resolve():
    N = int(input())
    if 10**(len(str(N))-1) == N:
        print("10")
    else:
        print(sum(map(int, str(N))))
resolve()