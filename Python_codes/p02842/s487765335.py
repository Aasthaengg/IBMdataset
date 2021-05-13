# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

N = int(input())

Xf = N / 1.08

if int(Xf) == Xf:
    print(int(Xf))
elif int((int(Xf)+1)*1.08) == N:
    print(int(Xf)+1)
else:
    print(":(")
