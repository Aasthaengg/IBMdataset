# n , m , l = map(int , input().split())

# list_n = list(map(int , inpuut().split()))<Paste>

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]


A, B, C = map(int, input().split())

n = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    if A == B and B == C:
        n = -1
        break

    An = (B + C) // 2
    Bn = (A + C) // 2
    Cn = (A + B) // 2

    A = An
    B = Bn
    C = Cn
    n += 1

print(n)
