def actual(N, D):
    return len(set(D))

N = int(input())
D = [int(input()) for _ in range(N)]

print(actual(N, D))